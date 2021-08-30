from time import sleep
import requests
import json
import sys

try:
    while True:
        response = requests.get("https://api.binance.us/api/v3/ticker/price?symbol=DOGEUSD")
        output = response.json()
        data = json.dumps(output['price'])
        punctuation = '''"'''
        remove_punct = ""
        for character in data:
            if character not in punctuation:
                remove_punct = remove_punct + character
        price = remove_punct
        print('current price of doge: '+ price, end='\r')


except KeyboardInterrupt:
    exit()