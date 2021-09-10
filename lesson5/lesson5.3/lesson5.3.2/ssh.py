import ip2cord
from ip2cord import ip2cord
import requests
import json

API_KEY = "fb333f10f9354cfebc3231023210909"
cord = ip2cord()

api_response = requests.get("http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + cord +"&aqi=no")

