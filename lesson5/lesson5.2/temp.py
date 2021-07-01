from time import sleep
import requests
import json

try:
    geolocation = requests.get("https://get.geojs.io/v1/ip/geo.json")
    geolocation_output = geolocation.json()
    geolocation_data_lon = json.dumps(geolocation_output['longitude'])
    geolocation_data_lat = json.dumps(geolocation_output['latitude'])
    punctuation = '''"'''
    remove_punct = ""
    for character in geolocation_data_lat + geolocation_data_lon:
        if character not in punctuation:
            remove_punct = remove_punct + character
    lat_removed_quotes = remove_punct
    edit = lat_removed_quotes[:7] +"," + lat_removed_quotes[7:]
    lat_and_lot = "https://api.weather.gov/points/"+ edit
    weather_api = requests.get(lat_and_lot)
    weather_api_output = weather_api.json()
    weather_api_link = json.dumps(weather_api_output['properties']['forecast'])
    for character in weather_api_link:
        if character not in punctuation:
            remove_punct = remove_punct + character 
    weather_api_link_removed_quotes = remove_punct
    finally_product = requests.get(weather_api_link_removed_quotes)
    finally_product_output = finally_product.json()
    the_temp = json.dumps(finally_product_output['1']['temperature'])
    print(the_temp)


except KeyboardInterrupt:
    exit()