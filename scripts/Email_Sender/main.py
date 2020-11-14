
import csv
from datetime import date
import yagmail

yag_smtp_connection = yagmail.SMTP( user="sunder7124@gmail.com", password="a1c3d4e5", host='smtp.gmail.com')

today = date.today()
d1 = today.strftime("%d-%m")

f = open('BirthdayData.csv')
csv_f = csv.reader(f)

for row in csv_f:
         if row[0] == d1:
             print (row[1])
             print (row[2])
             subject = 'HAPPY BIRTHDAY'
             contents = """Happy Birthday %s,
We wish you a very much happy Birthday
"""%(row[1])
             image = [yagmail.inline(row[3])]
             yag_smtp_connection.send(row[2], subject, contents, image)
             