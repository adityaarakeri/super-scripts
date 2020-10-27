# Weather Logger
This is a small script which pulls current weather conditions from the OpenWeatherMap API and logs it to a MySQL database.  

I use the database to feed a Grafana dashboard, but it has many applications.

## Requirements

* Python 3 (this is being used on Python 3.6.9)
* MySQL (using 14.14 Distrib 5.7.30)
* PyMySQL
* requests
* [OpenWeatherMap API Key](https://openweathermap.org/api)
* crontab (optional)

## Included Files

* requirements.txt
* database.xml - XML Schema of the database structure

## Usage
To log current conditions:  
`python3 weather_logger.py`

If you are wanting to store historic data, add to a crontab.  This example pulls current weather every 15 minutes:  
`*/15 * * * * python3 /path/to/script/weather_logger.py > /dev/null`

## Changes
The API documentation lists the available fields.  One would just need to make the necessary edits to what is extracted from the JSON request and the field mappings in the database.
