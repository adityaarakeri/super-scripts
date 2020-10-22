from selenium import webdriver
import urllib.request
#put your path of chrome driver instead of mine.
browser=webdriver.Chrome('C:\\Users\\viral\\Desktop\\ISB\\day 2\\chromedriver_win32\\chromedriver.exe')

user_h=input('Enter the user handle of the profile: ')

url='https://www.instagram.com/'
url_p=url+user_h+'/'
browser.get(url_p)

try:
	image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')

except:
	image=browser.find_element_by_xpath('//img[@class="be6sR"]')

img_link=image.get_attribute('src')
path="PATH WHERE YOU WANT TO SAVE DP"+ user_h+".jpg"
urllib.request.urlretrieve(img_link, path)
print('pic has been downloaded')


