# A simple program which scrapes desired information from websites
# Use the below code only for educational purposes
# Make sure the web-page which you scrape allows you to do it. And its a public web-page

import requests
import bs4

# Add proxy setting if you are behind a proxy server, or you can ignore the below
proxies = {
 "http": "http://115.125.91.31:9480",
 "https": "http://115.125.91.31:9480",
}

# Getting the web-content and storing it in res
res = requests.get('https://en.wikipedia.org/wiki/Machine_learning', proxies=proxies)

# Converting it to a BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'lxml')

A = []

# Loop around to get the texts from the Table-Of-Contents from: https://en.wikipedia.org/wiki/Machine_learning
# Inspect it and find what is common between all of them
# Since, we are extarcting the Table-Of-Contents, the common thing is the class. Here class is represented as ".", hence, .toc
for i in soup.select('.toc'):
    A.append(i.text)
    print(i.text) # Optional line

# Writing the extraction to a file
file1 = open("myfile.txt","w")
file1.writelines(A)
file1.close()

# End
