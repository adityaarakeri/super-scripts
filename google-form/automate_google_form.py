from selenium import webdriver
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import random

# open chrome and then open stackoverflow to directly bypass the secure login and captcha
driver = webdriver.Chrome()
driver.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A9b15b0994c6df9fc%2C10%3A1591711286%2C16%3A66b338ce162d6599%2Ca78a0c663f0beb12c0559379b61a9f5d62868c4fbd2f00e46a86ac26796507a1%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22921f8f04441041069683cc2377152422%22%7D&response_type=code&o2v=1&as=NCQvtBXI4prkLLDbn4Re0w&flowName=GeneralOAuthFlow')
# sleep time is provided so that the browser doesn't feel that you're a bot and doesn't ask for captcha
time.sleep(10)
# add your email id (it is preferred to enter the domain registered id to bypass the secure login and captcha, also you should not have two factor authentication)
# ENTER YOUR EMAIL ADDRESS AT THE PLACE OF <your-email-address>
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('<your-email-address>')
driver.find_element_by_xpath( '//*[@id="identifierNext"]/div/button' ).click()

time.sleep(5)

# ENTER YOUR PASSWORD AT THE PLACE OF <your-password>
driver.find_element_by_name( 'password' ).send_keys( "<your-password>" )
driver.find_element_by_xpath( '//*[@id="passwordNext"]/div/button' ).click()

time.sleep(5)
#this will open google.com just to make sure that you're logged in
driver.get('https://www.google.de/?hl=de')
# this is an infinite loop which will open the google form infinite times and fill it and save it.
while (True):
    # enter your form link here, this is a test link.
    driver.get('https://forms.gle/BzdB8kXEYny11aoL6')
    time.sleep(10)
    # short answer type question
    name1 = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
    name1[0].send_keys('Jayant Ojha')
    time.sleep(1)
    #radio button click
    radioElement = driver.find_elements_by_class_name('docssharedWizToggleLabeledContent')
    print(radioElement)
    radioElement[0].click()
    time.sleep(1)
    #checkbox click
    driver.find_elements_by_class_name('quantumWizTogglePapercheckboxInnerBox')[0].click()
    time.sleep(1)
    # upload file
    addFile = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/span/span[2]')
    addFile.click()
    # get to context of dialog box in iframe
    iframe = driver.find_element_by_class_name('picker-frame')
    driver.switch_to.frame(iframe)
    input_field = driver.find_element_by_xpath('//input[@type="file"]')
    # ADD PATH TO FILE WHICH YOU WANT TO UPLOAD FROM PC, REPLACE <path to file>
    input_field.send_keys('<path to file>')
    upload_image=driver.find_element_by_xpath('//*[@id="picker:ap:0"]')
    upload_image.click()
    time.sleep(15)
    #switch back to default context 
    driver.switch_to.default_content()
    # click submit button 
    submitButton = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submitButton.click()