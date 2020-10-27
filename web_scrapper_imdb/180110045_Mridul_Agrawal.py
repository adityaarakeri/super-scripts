import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('assign.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS moviedetails (title TEXT , released_date TEXT ,duration TEXT , description TEXT , rating TEXT , url TEXT)')

def data_entry(i):
    c.execute("INSERT INTO moviedetails (title, released_date, duration, description, rating, url) VALUES (?,?,?,?,?,?)",
              (title[i],date[i],duration[i],description[i],rating[i],movies[i]))
    conn.commit()
    
    
URL = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

movies=[]
rating = []
description = []
duration = []
title = []
date = []


table = soup.findAll('td', attrs = {'class':'titleColumn'})


for row in table:
    movie = {}
    movie['url']=row.a['href']
    movies.append(movie)

print(movies)

for i in range(0,250):
        movies[i] = str(movies[i])
        movies[i]=(movies[i][9:-2])
        movies[i]= 'https://www.imdb.com' + movies[i]

for i in range(0,250):        
    r = requests.get(movies[i])
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.findAll('div', attrs = {'class':'ratingValue'})
    for row in table:
        rating.append(row.strong.text)
        
    table = soup.findAll('div', attrs = {'class':'widget_inline_blurb'})
    for row in table:
        title.append(row.a.text)

    table = soup.findAll('div', attrs = {'class':'subtext'})
    for row in table:
        duration.append(row.time.text)

    table = soup.findAll('a', attrs = {'title':'See more release dates'})
    for row in table:
        date.append(row.text)

    table = soup.findAll('div', attrs = {'class':'summary_text'})
    for row in table:
        description.append(row.text)
    print(i)
    date[i] = date[i][:-1]
    description[i]=description[i][21:-13]
    duration[i] = duration[i][25:-21]
    
rows = zip(title,date,duration,description,rating,movies)

create_table()
for i in range(0,250):
    data_entry(i)
c.close()
conn.close()

#with open("output.csv", "w") as f:
 #   writer = csv.writer(f)
  #  for movie in rows:
   #     writer.writerow([movie])

