# No more dumb christmas refrences

now that we have our api key we can get our script to work \
make sure you remember your api key because its important. \
in your working file write this down
``` python
from requests.models import Response
import ip2cord
from ip2cord import ip2cord
import requests
import json
import sys
from time import sleep

API_KEY = "YOUR_API_KEY"
cord = ip2cord()

while True:
    sleep(5)
    api_response = requests.get("http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + cord +"&aqi=no")
    output = api_response.json()
    temp = json.dumps(output['current']['temp_f'])
    print(temp + "F", end='\r')
    sys.stdout.flush()
```