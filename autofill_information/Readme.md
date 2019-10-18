# Autofill Information Script
Simple python script allows user to autofill informations like name, address, email into different websites.

I have also developed a chrome extension with more functionality like, auto update and password manager. If you are interested then check https://github.com/pcube99/Autofill-Chrome-Extension

This flask application allows user to simply save their data and links online database, and it also provides support of deleting 
the saved details. 

## How to run ?

1) First dowload or clone the zip file.

2) Extract it at your desired location.

3) Install Python3 from below link https://www.python.org/downloads/

4) Install dependencies.
```
pip install selenium 
pip install beautifulsoup
pip install numpy
```
5) Install geckodriver.
```
https://www.guru99.com/gecko-marionette-driver-selenium.html
```
6) execute python script by running
```
python3 autofill_information.py "site name"(without quotes)
for example : python3 autofill_information.py http://www.spoj.com/register

```

