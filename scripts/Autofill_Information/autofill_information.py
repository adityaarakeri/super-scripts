from selenium import webdriver
from bs4 import BeautifulSoup
import shlex
import re
import sys
import numpy as np
import time
URL = sys.argv[1]
browser = webdriver.Firefox()
browser.get(URL)
content = browser.page_source
soup = BeautifulSoup(content, "lxml")
html_data = []
data_itr=0
for t in soup.select('input'):
    html_dict = {}
    x = str(t).split(" ")
    if(('type="text"' in str(t) or 'type="password"' in str(t) or 'type="email"' in str(t) ) and 'hidden="hidden"' not in str(t)):
        num = str(t).find("id=")
        itr = num+4
        id_string = ""
        while(str(t)[itr] != '"'):
            id_string += str(t)[itr]
            itr+=1
        html_dict['id'] = id_string
        
        #FIND NAMES
        num = str(t).find("name=")
        itr = num+6
        id_string = ""
        while(str(t)[itr] != '"'):
            id_string += str(t)[itr]
            itr+=1
        html_dict['name'] = id_string
        html_dict['dname'] = id_string.lower()

        #FIND AREA LABEL
        num = str(t).find("area-label=")
        itr = num+20
        id_string = ""
        while(str(t)[itr] != '"'):
            id_string += str(t)[itr]
            itr+=1
        html_dict['area-label'] = re.sub('[^A-Za-z0-9]+', '', id_string.lower())
        html_data.append(html_dict)


#print(html_data)

#DATA OF USER
fname = "John"
lname = "doe"
emaill = "jdoe@gmail.com"
passwordd = "123"
address1 = "22b baker street"
address2 = "Nr. Water park"
city = "Gandhidham"
state = "Gujarat"
gender = "Male"
phone_no = "1234566789"
zipcode = "124121"
username = "Hello_world"
full_name = "John Doe"
atts = ['firstname','lastname', 'email', 'password', 'address1','address2','city','state','zipcode','gender', 'phone_no', 'username','name' ]
data_values = {}
data_values[atts[0]] = fname
data_values[atts[1]] = lname
data_values[atts[2]] = emaill
data_values[atts[3]] = passwordd
data_values[atts[4]] = address1
data_values[atts[5]] = address2
data_values[atts[6]] = city
data_values[atts[7]] = state
data_values[atts[8]] = zipcode
data_values[atts[9]] = gender
data_values[atts[10]] = phone_no
data_values[atts[11]] =username
data_values[atts[12]] = full_name
#print(len(atts))
flag = np.zeros(len(html_data))
for i in range(0,len(html_data)):
    try:
        for j in range(0,len(atts)):
            if(atts[j] in html_data[i]['dname'] and flag[i] == 0):
                try:
                    browser.find_element_by_id(html_data[i]['id']).send_keys(data_values[atts[j]])
                    flag[i]=1
                except:
                    flag[i]=0
                
            if(atts[j] in html_data[i]['area-label'] and flag[i] == 0):
                try:
                    browser.find_element_by_id(html_data[i]['id']).send_keys(data_values[atts[j]])
                    flag[i]=1
                except:
                    flag[i]=0
                
            if(atts[j] in html_data[i]['dname'] and flag[i] == 0):
                try:
                    browser.find_element_by_name(html_data[i]['name']).send_keys(data_values[atts[j]])
                    flag[i]=1
                except:
                    flag[i]=0
                
            if(atts[j] in html_data[i]['area-label'] and flag[i] == 0):
                try:
                    browser.find_element_by_name(html_data[i]['name']).send_keys(data_values[atts[j]])
                    flag[i]=1
                except:
                    flag[i]=0
                
    except:
        print("not working")