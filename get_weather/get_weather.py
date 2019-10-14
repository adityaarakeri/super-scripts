import argparse
import os
from pyowm import OWM, exceptions

parser = argparse.ArgumentParser(description='Latest weather for a city')
parser.add_argument('city', type=str, help='name of city to display current weather conditions')
city = parser.parse_args().city

owm = OWM(os.environ.get("API_KEY"))

try:
  observation = owm.weather_at_place(city)
  weather = observation.get_weather()

except exceptions.api_response_error.UnauthorizedError:
  error_msg = "Invalid OpenWeatherMap API key"
  error_msg += "\nSign up for an API key at https://home.openweathermap.org/users/sign_up"
  error_msg += "\nNote a new API can take up to 2 hours to be activated"
  print(error_msg)

except exceptions.api_response_error.NotFoundError:
  error_msg = "Cannot fetch weather for {}".format(city)
  error_msg += "\nPlease enter a valid city name, e.g."
  error_msg += "\n  - chicago"
  error_msg += "\n  - \"hong kong\""
  error_msg += "\n  - \"sydney, australia\""
  error_msg += "\n  - \"London, GB\""
  print(error_msg)

else:
  weather_status = weather.get_detailed_status()
  temperature_F = weather.get_temperature(unit="fahrenheit")
  temperature_C = weather.get_temperature(unit="celsius")
  cloud = weather.get_clouds()
  humidity = weather.get_humidity()
  rain = weather.get_rain()
  snow = weather.get_snow()

  weather_summary = {
    'weather': weather_status if bool(weather_status) else {},
    'temperature': "{}C / {}F".format(round(temperature_C['temp']), round(temperature_F['temp'])) if bool(temperature_F) else {},
    'cloud coverage': "{}%".format(cloud) if bool(cloud) else {},
    'humidity': "{}%".format(humidity) if bool(humidity) else {},
    'rain': "{}mm in the last hour".format(rain['1h']) if (bool(rain) and '1h' in rain.keys()) else {},
    'snow': "{}mm in the last hour".format(snow['1h']) if (bool(snow) and '1h' in snow.keys()) else {}
  }

  heading = "{} weather provided by OpenWeatherMap".format(observation.get_location().get_name())
  print(heading)
  print("-"*len(heading))
  for key, value in weather_summary.items():
    if bool(value):
      print("{}: {}".format(key, value))