# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:29:38 2020

@author: Ujjwal Kumar
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

def send_text(rep_count =1 , intractive = True,print_log = True):

	# Replace below path with the absolute path 
	# to chromedriver in your computer 
	driver = webdriver.Chrome('C:/Users/Ujjwal Kumar/Downloads/chromedriver_win32/chromedriver.exe') 

	driver.get("https://web.whatsapp.com/") 
	wait = WebDriverWait(driver, 600)

	if print_log : print("Scan QR Code, And then Enter")

	contact = input("Enter Conatct : ")
	text = input("Enter Your Message : ")

	if print_log : print("Contact and message set ")

	inp_xpath_search = "//div[@class='_3FRCZ copyable-text selectable-text']"
	input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
	input_box_search.send_keys(contact)
	time.sleep(2)

	if print_log :print("Conatct Name  passed in Search Box ")
	if intractive : 
		cont = input("Continue ? [Y/N] :")
		if cont in ['Y','y']:
			print("continued----")
		else:
			return

	if print_log : print("Search Value Passed ")
	if intractive : 
		cont = input("Continue ? [Y/N] :")
		if cont in ['Y','y']:
			print("continued----")
		else:
			return

	selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"'][1]")
	selected_contact.click()
	if print_log : print("Enterd Chat Window ")
	if intractive : 
		cont = input("Continue ? [Y/N] :")
		if cont in ['Y','y']:
			print("continued----")
		else:
			return

	inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
	input_box = driver.find_element_by_xpath(inp_xpath)
	time.sleep(2)
	if print_log : print("Chat Text Box Found ")
	if intractive : 
		cont = input("Continue ? [Y/N] :")
		if cont in ['Y','y']:
			print("continued----")
		else:
			return
	for i in range(rep_count):
		input_box.send_keys(text + Keys.ENTER)
	time.sleep(2)
	driver.quit()

def automation_launcher():
	print("Hi , How May I help You ")
	print("1.Send Repetative Text \n2.Send Single Text")
	choice_1 = input("Your Choice :")
	msg_count = 1
	if choice_1 == 1:
		msg_count = input("enter repetation Count:")
	choice_2 = input(" You want me to work on full Automation ? [Y/N] :")
	if choice_2 in ['Y','y']:
		send_text(rep_count = msg_count,intractive=False)
	else:
		send_text(rep_count = msg_count)






if __name__ == '__main__':
	# Launch Automation 
	automation_launcher()
else:
	print("Called with Name "+__name__)
