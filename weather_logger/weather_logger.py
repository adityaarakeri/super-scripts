#!/usr/bin/python3

# Uses the OpenWeatherMap API to download current weather conditions and logs it to a MySQL database for use in a Grafana Dashboard.  Could have many other applications as well.  

# Usage for current data:  ./weather_logger.py
# Set up a cronjob to get results over time (every 10-15 minutes is probably sufficient for most uses)

import requests
import json
import pymysql.cursors

# OpenWeatherMap API Key
key = 'abcdefghijklmnopqrstuvwxyz123456' 

# Location Info - Easiest way to get this is to look up the weather on OpenWeatherMap's website and note what codes are used in the URL
city = 'SomeCity' #Your City
state = 'aa' # Your State
country = 'us' # Your County

# Database Connection Info - see database.xml for the schema
dbHostname = "localhost" # Using a self-hosted MySQL database - change to server address if using an external server
dbUsername = "db_user"
dbPassword = "db_password"
dbTable = "db_table"

# Send request to the API
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={key}&units=imperial")

# Data comes back in JSON format
data = response.json()

# Splitting out desired data points
temp = data['main']['temp']
feel = data['main']['feels_like']
pressure = data['main']['pressure']
humidity = data['main']['humidity']

# Left for debugging what info the API was returning
#print("Temp: ", temp)
#print("Feels like: ", feel)
#print("Pressure: ", pressure, "kPa")
#print("Humidity: ", humidity, "%")

# Make the connection to the database and insert the received values
connection = pymysql.connect(dbHostname,dbUsername,dbPassword,dbTable)
cursor = connection.cursor()
sql = "INSERT INTO weather (temp, feelsLike, pressure, humidity) VALUES (%s,%s,%s,%s)"
cursor.execute(sql,(temp,feel,pressure,humidity))
connection.commit()
cursor.close()
connection.close()

