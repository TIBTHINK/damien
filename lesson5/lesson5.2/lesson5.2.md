# I am once again Requesting your json

Its always good to get information from the outside world 

in this lesson we are going to get working on a script that \
fetches a api to find the current price of doge coin
```python
# Importing required libraries
from time import sleep
import requests
import json
import sys

try:
    while True:   
        response = requests.get("https://api.binance.us/api/v3/ticker/price?symbol=DOGEUSD")    # Requesting binance api for current price
        output = response.json()    # Saving the request as a json varibal
        data = json.dumps(output['price'])  # Parsing the repsones for current price
        punctuation = '''"'''                           # this
        remove_punct = ""                               # is
        for character in data:                          # to 
            if character not in punctuation:            # make
                remove_punct = remove_punct + character # it
        price = remove_punct                            # fancy
        print('current price of doge: '+ price, end='\r') 

except KeyboardInterrupt:
    exit()
```