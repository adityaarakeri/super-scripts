#!/usr/bin/env python3

import requests, bs4

url = input("Enter the start page: ")
nimages = int(input("Enter the number of images to be downloaded: "))

url = url + "&page="
page_count=1

while nimages > 0:

    url_data = requests.get(url+str(page_count))

    page_count = page_count+1

    soup = bs4.BeautifulSoup(url_data.text)

    images = soup.select("div.thumb-container-big ")

    for image in images:
        if image.find('div').findChildren()[3].find('span').find('span').text == "1920x1080":
            src_link = image.find('div').find('div').find('a').find('img').get('data-src')
            src_break = src_link.split('/')
            src_break[-1] = src_break[-1][10::]
            src_link = "/".join(src_break)

            full_image = requests.get(src_link)
            ifile = open(str(image.get('id'))+".jpg","wb")
            ifile.write(full_image.content)
            ifile.close()

            nimages = nimages-1
            if nimages < 0:
                break
