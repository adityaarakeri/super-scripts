from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from getpass import getpass

class Inst:
    def __init__(self):
        Address=input("Enter your Gmail address: ")
        pw=getpass()
        link=input("Enter the Google Meet link: ")
        duration=int(input("Duration of your lecture [STRICTLY IN SECONDS e.g type 3600 for 1 hr]: "))
        options = Options();
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2,"profile.default_content_setting_values.media_stream_camera": 2})
        options.add_argument("--use-fake-ui-for-media-stream=0")
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
        self.driver.get("https://accounts.google.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")\
            .send_keys(Address) #Your Gmail address goes here
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")\
            .send_keys(pw) #Your password goes here
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")\
            .click()
        sleep(5)
        self.driver.get(link)
        sleep(4)
        #self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")\
         #   .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div/div")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div")\
            .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/span/span")\
            .click()
        sleep(duration)
        self.driver.quit()


Inst()
