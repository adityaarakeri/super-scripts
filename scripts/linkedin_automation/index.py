import os,random,sys,time
#from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome('./driver/chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login')

file=open('./config.txt')
lines=file.readlines()
username=lines[0]
password=lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID =browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

content=requests.get('https://www.linkedin.com/in/rohan-devaki')
soup = BeautifulSoup(content.text, 'html.parser')
 
visitingProfileID='/in/rohan-devaki'
fullLink='https://www.linkedin.com/'+ visitingProfileID
browser.get(fullLink)

visitedProfiles = []
profilesQueued=[]

def getNewProfileIDs(soup,profilesQueued):
    profilesID=[]
    pav= soup.find('section',{'class':'artdeco-card ember-view'})
    all_links=pav.findAll('a',{'class':'pv-browsemap-section__member ember-view'})
    for link in all_links:
        userID=link.get('href')
        if(userID not in profilesQueued) and (userID not in visitedProfiles):
            profilesID.append(userID)
    return profilesID

profilesQueued=getNewProfileIDs(BeautifulSoup(browser.page_source), profilesQueued)

while profilesQueued:
    try:
        visitingProfileID=profilesQueued.pop()
        visitedProfiles.append(visitingProfileID)
        fullLink='https://www.linkedin.com' + visitingProfileID
        browser.get(fullLink)
        browser.find_element_by_class_name('artdeco-button__text').click()
        
        browser.find_element_by_class_name('mr1').click()
        
        customMessage = "Hello,This is social-sheduler,We would like to connect with you"
        elementID=browser.find_element_by_id('custom-message')
        elementID.send_keys(customMessage)
        
        browser.find_element_by_class_name('ml1').click()
        
        #add the id to visitedUsersFile
        with open('visitedUsers.txt','a') as visitedUsersFile:
            visitedUsersFile.write(str(visitingProfileID)+ '\n')
        visitedUsersFile.close()
        
        #get noe profiles ID
        soup=BeautifulSoup(browser.page_source)
        try:
            profilesQueued.extend(getNewProfileIDs(soup,profilesQueued))
        except:
            print('Continue')
            
        #pause
        time.sleep(random.uniform(5,15)) #otherwise,sleep to make sure that it is not automated process
        
        if(len(visitedProfiles)%50==0):
            print('Visited Profiles:',len(visitedProfiles))
            
        if(len(profilesQueued)>10000):
            with open('profilesQueued.txt','a') as visitedUsersFile:
                visitedUsersFile.write(str(visitingProfileID)+'\n')
            visitedUsersFile.close()
            print('100,000 Done!!!')
            break;
    except:
        print('error')