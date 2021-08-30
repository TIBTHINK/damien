# Importing required libraries
from time import sleep
import requests
import json
import sys

try:        # Havinging the code run in a try function so if we cancle it we dont get errors
    while True:     # A forever loop to get current price 
        response = requests.get("https://api.binance.us/api/v3/ticker/price?symbol=DOGEUSD")    # Requesting binance api for current price
        output = response.json()    # Saving the request as a json varibal
        data = json.dumps(output['price'])  # Parsing the repsones for current price
        punctuation = '''"'''                           # this
        remove_punct = ""                               # is
        for character in data:                          # to 
            if character not in punctuation:            # make
                remove_punct = remove_punct + character # it
        price = remove_punct                            # fancy
        print('current price of doge: '+ price, end='\r') #printing the price from the api and updating the line instead of making a new one every loop


except KeyboardInterrupt:
    exit()