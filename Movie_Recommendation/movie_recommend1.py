from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP
def f1():
    count = 0
    l=[]
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
            #results['text']=tmp[1][:-3]
            l.append(tmp[1][:-3])
        if (count > 11):
            break
        count += 1

    results['text'] ='Sad Movies acc.to IMDB'+':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0],l[1],l[2],l[3],l[4])
    l=[]
    print()
    print()


def f2():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()
    results['text'] = 'Disgust Movies acc.to IMDB' + ': %s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []


def f3():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()
    results['text'] = 'Anger Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []


def f4():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()
    results['text'] = 'Anticipation Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []


def f5():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()
    results['text'] = 'Fear Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []


def f6():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()
    results['text'] = 'Enjoyment Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []



def f7():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 11):
            break
        count += 1
    print()
    print()
    results['text'] = 'Trust Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []



def f8():
    count = 0
    l=[]
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
            l.append(tmp[1][:-3])
        if (count > 13):
            break
        count += 1
    print()
    print()
    results['text'] = 'Surprise Movies acc.to IMDB' + ':%s \n * %s \n * %s\n *%s\n *%s\n' % (l[0], l[1], l[2], l[3], l[4])
    l = []

def f9():
    exit()


root = Tk()
C=Canvas(root,height=500,width=600)
fl=PhotoImage(file="super.png")
background_label=Label(root,image=fl,bg="pink")
background_label.place(x=0,y=0,relwidth=1,relheight=1)
C.pack()
one = Label(root, text="MOVIE RECOMMENDATION APP",font=60,bg="blue", fg="white")
one.place(x=0,y=0, relwidth=1)
two = Label(root, text="Choose any one of the emotions", bg="green", fg="white",font=60)
two.place(x=0,y=20,relwidth=1)
three = Label(root, text="EMOTIONS ARE AS FOLLOWS", font=60,fg="black",bg="lightblue")
three.place(x=0,y=40,relwidth=1)
lower_frame = Frame(root, bg='#42c2f4', bd=5)
lower_frame.place(x=300,y=336,relwidth=0.5, relheight=0.3, anchor='n')
bg_color = 'lightgreen'
#,relx=0.5, rely=0.25,

results = Label(lower_frame, bg=bg_color,fg="blue",anchor='center', justify='left', bd=4,)
results.config(font=40)
results.place(relwidth=1, relheight=1)

button1 = Button(root, text="SAD", fg="red", command=f1)
button2 = Button(root, text="DISGUST", fg="blue", command=f2)
button3 = Button(root, text="ANGER", fg="green", command=f3)
button4 = Button(root, text="ANTICIPATION", fg="purple", command=f4)

button5 = Button(root, text="FEAR", fg="red", command=f5)
button6 = Button(root, text="ENJOYMENT", fg="blue", command=f6)
button7 = Button(root, text="TRUST", fg="green", command=f7)
button8 = Button(root, text="SURPRISE", fg="purple", command=f8)
button9 = Button(root, text="EXIT", fg="red", command=f9)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.place(x=0,y=0)


root.mainloop()



