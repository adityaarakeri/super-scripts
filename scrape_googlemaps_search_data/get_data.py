from selenium import webdriver
import time
import csv

def writeToCsv(name: str, phone: str, email: str, link: str, csvname):
    with open('%s.csv' %csvname, 'a', newline='') as csvfile:
        fieldnames = ['name', 'phone','email','link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #if not exists(name):
        writer.writerow({'name': name, 'phone': phone, 'email': email, 'link': link})

search_keywords = ['gym','dance',] #list of key words for which data need to be scraped
def search(keywords,no_searches):
    for key in keywords:
        keyword = key
        keyword = keyword.replace(' ','+')
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/maps/search/"+keyword+"/")
        time.sleep(1)
        counter = no_searches + 1
        for _k in range((no_searches//20 +1)):
            for i in range(0,20):
                counter-=1
                if(counter ==0):
                    break
                time.sleep(4)
                while True:
                    try:
                        searches = driver.find_elements_by_class_name("section-result-content")
                        title = searches[i].find_element_by_class_name("section-result-title")
                    except IndexError:
                        continue
                    break

                name=(title.text)
                xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "section-info-line", " " ))]'
                searches[i].click()
                time.sleep(2)
                info_sections = driver.find_elements_by_xpath(xpath)
                eorw=[]
                phone =''
                for j in info_sections:
                    try:
                        phone = int((j.text).replace(' ', ''))
                    except ValueError:
                        k = j.text
                        if (
                            k.endswith('.net') or
                            k.endswith('.com') or
                            k.endswith('.in') or
                            k.endswith('.gov') or
                            k.endswith('.org') or
                            k.endswith('.me')):
                            eorw.append(j.text)

                driver.execute_script(script="window.history.back(-1);")
                time.sleep(1)
                mail =''
                site = ''
                for l in eorw:
                    if '@' in l:
                        mail = l
                    else:
                        site = l
                        site.replace('Menu\n','')
                writeToCsv(name,phone,mail,site,key)
                print(name,phone,mail,site)
            time.sleep(2)
            next = driver.find_element_by_xpath('//*[@aria-label=" Next page "]')
            next.click()
        driver.quit()

search(search_keywords,30)
