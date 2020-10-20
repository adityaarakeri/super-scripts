#!/user/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
import json, csv, re
import argparse, getpass

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def opt_parser():
    """Parse command-line options."""
    # verbose, headless, json, csv, html, htmlpage, loginfile
    parser = argparse.ArgumentParser(description="Use Selenium & Firefox to automate Facebook login and scrape user's friend list.",
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99))
    parser.add_argument("-v", "--verbose", help="Increase verbosity level.", action="store_true", default=False, dest="verbose")
    parser.add_argument("-b", "--headless", help="Activate headless mode, run firefox in the background.", action="store_true", default=False, dest="headless")
    parser.add_argument("-t", "--timeout", help="Time to wait for elements to load on webpages before giving up. (30s)", type=int, default=30, dest="timeout")
    parser.add_argument("-j", "--json", help="Export user's friend list in JSON format. (default)", default=True, action="store_true", dest="json")
    parser.add_argument("-c", "--csv", help="Export user's friend list in CSV format.", default=False, action="store_true", dest="csv")
    parser.add_argument("-s", "--html", help="Export the source html page.", default=False, action="store_true", dest="html")
    parser.add_argument("-i", "--import-html", help="Import data from source html page.", default=None, dest="htmlpage")
    parser.add_argument("-l", "--login-data", help="Read login data from file.", default=None, dest="loginfile")
    return parser.parse_args()

def check_page_loaded(driver):
    """Check whether the page is loaded or not. """
    try:
        existing = False
        elements = driver.find_elements_by_class_name("uiHeaderTitle")

        for element in elements:
            if (element.get_attribute('innerHTML') == "More About You"):
                existing = True

        return existing

    except:

        return False

def sec_to_hms(sec):
    """ Convert seconds to hh:mm:ss format. """
    h = sec / 3600
    sec %= 3600

    m = sec / 60
    sec %= 60

#    return '%02d:%02d:%02d' % (h, m, sec)
    return '{:02}:{:02}:{:02}'.format(int(h), int(m), int(sec))

def export_as_csv(names, ids, filename):
    """Export user's friend list in CSV format. """

    with open(filename, mode='w+', encoding='utf-8') as ffile:
        writer = csv.writer(ffile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name', 'Facebook profile id'])

        for i in range(len(ids)):
            writer.writerow([ids[i], names[i][0], names[i][1]])

    return filename

def export_as_html(htmlpage, filename):
    """Export user's friend list source html page. """
    with open(filename, "w+", encoding="utf-8") as htmlfile:
        htmlfile.write(htmlpage)

    return filename

def export_as_json(names, ids, filename):
    """Export user's friend list in JSON format. """
    data = dict()
    data["number of friends"] = len(ids)
    data["friends"] = dict(zip(ids, names))

    with open(filename, "w+", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    return filename

def import_from_htmlfile(path_to_htmlfile):
    """Import friend list from htmlfile downloaded from a web browser. """
    with open(path_to_htmlfile, "r", encoding="utf-8") as htmlfile:
        htmlpage = htmlfile.read()

    return htmlpage

def get_login_data_from_stdin():
    """ Get login data from stdin. """
    print("Facebook Login:- ")
    user = input("Enter e-mail address or phone number: ")
    password = getpass.getpass("Enter password: ")

    return user, password

def get_login_data_from_file(filename):
    with open(filename, "r", encoding="utf-8") as login_file:
        user = login_file.readlines(1)
        password = login_file.readlines(1)

    return user, password

def automate(driver, user, password, timeout=30, verbose=False):
    """ Automate user interaction using selenium and return html source page."""
    wait = WebDriverWait(driver, timeout)
    facebook_url = "https://www.facebook.com/login.php"
    
    if verbose:
        print("GET", facebook_url)
    
    driver.get(facebook_url)

    elem = wait.until(EC.presence_of_element_located((By.ID, "email")))
    
    if verbose:
        print("Entering email... ")
    
    elem.send_keys(user)

    elem =  wait.until(EC.presence_of_element_located((By.ID, "pass")))

    if verbose:
        print("Entering password... ")
        print("Sending data... ")

    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    if verbose:
        print("Waiting for elements to load... timeout={0}".format(timeout))

    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/a")))
    if verbose:
        print("GET https://www.facebook.com/profile.php")

    driver.get("https://www.facebook.com/profile.php")

    while (driver.current_url == "https://www.facebook.com/profile.php"):
    	time.sleep(0.02)

    url = (driver.current_url[0:-2] if "#_" == driver.current_url[-2:] else driver.current_url) + "/friends"
    if verbose:
        print("GET", url)

    driver.get(url)
    if verbose:
        print("Scroling down... ")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if check_page_loaded(driver):
            break

    return driver.page_source

def get_source_htmlpage(options):
    """Start the program and handle command line options"""

    if options.loginfile:
        try:
            user, password = get_login_data_from_file(options.loginfile)
        except Exception as Error:
            print(Error)

            if 'y' in input("Do you want to get login data from stdout?(y/n) ").lower():
                user, password = get_login_data_from_stdin()

            else:
                sys.exit(0)
    else:
        user, password = get_login_data_from_stdin()

    if options.verbose:
        start_time = time.time()
        print("Running Firefox... ")

    firefox_options = Options()
    firefox_options.set_headless(headless=options.headless)

    ffprofile = webdriver.FirefoxProfile()
    ffprofile.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(firefox_profile=ffprofile, firefox_options=firefox_options)

    htmlpage = automate(driver, user, password, verbose=options.verbose, timeout=options.timeout)

    driver.quit()

    if options.verbose:
        print("Done downloading!.. ({0})\n".format( sec_to_hms(time.time() - start_time)) )

    return htmlpage

def extract_friend_list(htmlpage):
    """
        Extract user's friend list from html page using regex expressions only.
        This function should be removed soon.
    """
    
    ids = re.findall('friend_list_item.+?data-profileid="(.+?)"', htmlpage)
    names = re.findall('friend_list_item.+?aria-label="(.+?)"', htmlpage)

    return names, ids

def extract_friend_list(htmlpage):
    """Extract user's friend list from html page using BeautifulSoup and regex expressions."""
    friend_list_items = BeautifulSoup(htmlpage, "html.parser").find_all("li", class_="_698")
    names = []
    ids = []

    for item in friend_list_items:
    	try:
    		if (item.find_all("a")[2].text[0].isdigit()):
    			continue
    		names.append((item.find_all("a")[2].text, 0))
    		ids.append(re.findall("www.facebook.com\/(.+?)[&]?[a]?[m]?[p]?[;]?[\?]?fref=pb",
                       item.find_all("a")[2].attrs['href'])[0].replace("profile.php?id=",""))
    	except:
    		names.append((item.find_all("a")[1].text, 1))
    		try:
    			ids.append(item.find_all("a")[0].attrs['data-profileid'])
    		except:
    			continue

    return names, ids

def main():
    # verbose, headless, json, csv, html, htmlpage, loginfile, timeout
    options = opt_parser()

    if options.htmlpage:
        try:
            htmlpage = import_from_htmlfile(options.htmlpage)

        except Exception as error:
            print(error)

            if 'y' in input("Do you want to scrape data online?(y/n) ").lower():
                htmlpage = get_source_htmlpage(options)

            else:
                return 0

    else:
        htmlpage = get_source_htmlpage(options)

    if options.verbose:
        print("Processing data... ")

    names, ids = extract_friend_list(htmlpage)
    filename = 'facebook friends from {0}'.format(time.strftime("%Y-%m-%d %H-%M-%S"))

    if (len(names) != len(ids)):
        print("Unexpected error!..")
        print("Please send us your source html file.")
        print("kindly file an issue in our repository on github so we can fix this bug.")
        print("Github repository: https://github.com/Mhmd-Hisham/selenium_facebook_scraper.git")
        if options.html == False:
            if 'y' in input("Do you want to export the html page and send it manually?(y/n) ").lower():
                options.html = True
                print("Thank you for your support. ")

    print("{0} friends found!".format(len(ids)))

    if options.json:
        print("Exporting data as json file... ", end="", flush=True)
        export_as_json(names, ids, filename + ".json")
        print("Done. File: '{0}'.json".format(filename))

    if options.csv:
        print("Exporting data as csv file... ", end="", flush=True)
        export_as_csv(names, ids, filename + ".csv")
        print("Done. File: '{0}'.csv".format(filename))

    if options.html:
        print("Exporting source html page... ", end="", flush=True)
        export_as_html(htmlpage, filename + ".html")
        print("Done. File: '{0}'.html".format(filename))

    if 'y' in input("Print data to stdout?(y/n) ").lower():
        for i in range(len(ids)):
           print(names[i][0],"[Deactivated]" if names[i][1] else '', ":", ids[i])

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Keyboard Interruption! exitting... ")

    sys.exit(0)
