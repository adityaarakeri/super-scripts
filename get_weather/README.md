# :sunny: get_weather
A python script which can be run in the command line to print out a city's current weather.

## Pre-requisites
- Install all required packages:
```sh
$ pip install -r requirements.txt
```
- [Sign up](https://home.openweathermap.org/users/sign_up) for an API key from OpenWeatherMap (note an API key can take up to 2 hours to activate), then set up an environment variable:
```sh
$ export API_KEY
$ API_KEY="YOUR_API_KEY_HERE"
```

## Usage
```sh
$ python get_weather.py "CITY_NAME"
```

### Examples
```sh
$ python get_weather.py chicago
$ python get_weather.py "hong kong"
$ python get_weather.py "taupo, new zealand"
$ python get_weather.py "london, GB"
```