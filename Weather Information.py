import requests
from pprint import PrettyPrinter
import time

api_key = "ac6acb1b7507565b9453f400a022aa76"    # "openweathermap.org" provided personal api key
city = input("Enter your current city\n")
# basi url is taken from "https://openweathermap.org/current"
base_url = "http://api.openweathermap.org/data/2.5/weather" + "?q=" + city + "&appid=" + api_key #+ "&mode=html"
time.sleep(1)
weather_data = requests.get(base_url).json()
pp=PrettyPrinter(indent=2)
pp.pprint(weather_data)
