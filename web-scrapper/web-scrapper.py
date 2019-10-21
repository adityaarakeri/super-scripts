from selenium import webdriver

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
# For windows machine only
browser = webdriver.Chrome(executable_path = r'C:/New folder/chromedriver', chrome_options=option) #for windows machine

# Go to desired website
browser.get("https://github.com/TheDancerCodes")

# Get all of the pinned repo languages
language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("LANGUAGES:")
print(languages, '\n')
