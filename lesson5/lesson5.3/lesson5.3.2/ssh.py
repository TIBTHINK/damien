from requests.models import Response
import ip2cord
from ip2cord import ip2cord
import requests
import json
import sys
from time import sleep

API_KEY = "fb333f10f9354cfebc3231023210909"
cord = ip2cord()

while True:
    sleep(5)
    api_response = requests.get("http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + cord +"&aqi=no")
    output = api_response.json()
    temp = json.dumps(output['current']['temp_f'])
    print(temp + "F", end='\r')
    sys.stdout.flush()