# Google Form Automation
This selenium script in python opens up any google form, signs you in, bypasses captcha and browser realizing that you're a bot and can also fill that form in an infinite loop for unlimited number of times.

This script covers all use cases:
- short answer type
- radio buttons
- checkboxes
- file/image upload

## Requirements:
- selenium installation 
 `pip install selenium`
 - Web Driver: Selenium requires a driver to interface with the chosen browser.
 https://sites.google.com/a/chromium.org/chromedriver/downloads
 - for more installation details: 
 https://selenium-python.readthedocs.io/installation.html

## Changes in script to  be made
### (position is mentioned as comments in the script)
- enter your email address and password (position is mentioned as comments in the script)
- enter form link you want to fill
- enter file path you want to upload
- with a few tweaks to the script you can fill out any google form as many number of times as you want
