# Python3 Facebook Scraper

This is a simple python3 script used to download a user's friend list from facebook. The script uses selenium & Firefox to automate the login process and extract the data from the user's account. All you have to do is to write the email and password and the script will do all the work. Simple!

## Usage
```
user:~$ python3 facebook_scraper.py --help
usage: facebook_scraper.py [-h] [-v] [-b] [-t TIMEOUT] [-j] [-c] [-s] [-i HTMLPAGE] [-l LOGINFILE]

Use Selenium & Firefox to automate Facebook login and scrape user's friend list.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity level.
  -b, --headless        Activate headless mode, run firefox in the background.
  -t TIMEOUT, --timeout TIMEOUT
                        Time to wait for elements to load on webpages before giving up. (30s)
  -j, --json            Export user's friend list in JSON format. (default)
  -c, --csv             Export user's friend list in CSV format.
  -s, --html            Export the source html page.
  -i HTMLPAGE, --import-html HTMLPAGE
                        Import data from source html page.
  -l LOGINFILE, --login-data LOGINFILE
                        Read login data from file.

```

## Requirements
- Python (3+). [[How to install](https://realpython.com/installing-python/)]
- BeautifulSoup4 for python3. [[How to install](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)]
```
pip3 install bs4
```
- Selenium for python3. [[How to install](https://selenium-python.readthedocs.io/installation.html)]
```
pip3 install selenium
```
- Firefox webbrowser.   [[Windows](https://support.mozilla.org/en-US/kb/how-download-and-install-firefox-windows), [Linux](https://support.mozilla.org/en-US/kb/install-firefox-linux), [Mac](https://support.mozilla.org/en-US/kb/how-download-and-install-firefox-mac)]
- Geckodriver for Firefox. [[How to install](https://github.com/mozilla/geckodriver/releases/)]


