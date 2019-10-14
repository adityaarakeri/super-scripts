from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def f1():
    count = 0
    emotion = "Sad"
    print("SAD MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()



def f2():
    count = 0
    emotion = "Disgust"
    print("DISGUST MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()


def f3():
    count = 0
    emotion = "Anger"
    print("ANGER MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()


def f4():
    count = 0
    emotion = "Anticipation"
    print("ANTICIPATION MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()


def f5():
    count = 0
    emotion = "Fear"
    print("FEAR MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()


def f6():
    count = 0
    emotion = "Enjoyment"
    print("ENJOYMENT MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()



def f7():
    count = 0
    emotion = "Trust"
    print("TRUST MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()



def f8():
    count = 0
    emotion = "Surprise"
    print("SURPRISE MOVIES HAIN")
    urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    for i in title:
        tmp = str(i).split('>')
        if (len(tmp) == 3):
            print(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()



root = Tk()
C=Canvas(root,bg="blue",height=250,width=300)
fl=PhotoImage(file="background3.png")
background_label=Label(root,image=fl)
C.pack()
background_label.place(x=0,y=0,relwidth=1,relheight=1)
one = Label(root, text="Movie Recomendation App", fg="black")
one.pack()
two = Label(root, text="Choose any one of the emotions", bg="green", fg="white")
two.pack(fill=X)
three = Label(root, text="EMOTIONS ARE AS FOLLOWS", fg="black",bg="lightblue")
three.pack()

button1 = Button(root, text="SAD", fg="red", command=f1)
button2 = Button(root, text="DISGUST", fg="blue", command=f2)
button3 = Button(root, text="ANGER", fg="green", command=f3)
button4 = Button(root, text="ANTICIPATION", fg="purple", command=f4)

button5 = Button(root, text="FEAR", fg="red", command=f5)
button6 = Button(root, text="ENJOYMENT", fg="blue", command=f6)
button7 = Button(root, text="TRUST", fg="green", command=f7)
button8 = Button(root, text="SURPRISE", fg="purple", command=f8)

button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)
button4.pack(side=TOP)
button5.pack(side=TOP)
button6.pack(side=TOP)
button7.pack(side=TOP)
button8.pack(side=TOP)
root.mainloop()



