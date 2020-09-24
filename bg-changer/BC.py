import urllib2
import urllib
from bs4 import BeautifulSoup
stri = input()
listtocheck = [stri]
ctr = 0
for i in listtocheck:
	print(i)
	resp = urllib2.urlopen(i)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if link["href"].startswith("/"):
			if not i+link["href"] in listtocheck:
				listtocheck.append(i+link["href"])
				print (i+link["href"])
		elif link["href"].endswith("jpg"):
			urllib.urlretrieve(i+"/"+link["href"], link["href"]+".jpg")
		for img in soup.find_all("img",src = True):
			if	int(urllib.urlopen(i+img["src"]).info()["Content-Length"])>100000.0:
				print (urllib.urlopen(i+img["src"]).info()["Content-Length"])
				urllib.urlretrieve(i+img["src"], str(ctr)+".jpg")
				ctr+=1;