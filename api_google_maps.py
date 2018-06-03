'''
APIs
'''

import requests
from bs4 import BeautifulSoup


# XML
with open('example.html', 'r') as f:
    xml = f.read()

b = BeautifulSoup(xml, 'xml')

# find the fourth topic


# collect data from google maps api
# documentation: https://developers.google.com/maps/documentation/geocoding/start
address = 'general assembly dc'
api_url = r'https://maps.googleapis.com/maps/api/geocode/xml?address={}'.format(address)
r = requests.get(api_url)
b = BeautifulSoup(r.text, 'xml')

# find the status code


# find the postal code


# find the latitude and longitude
latitude = ''
longitude = ''

# use a python api wrapper package for google maps
# https://github.com/googlemaps/google-maps-services-python
import googlemaps  

# instantiate an api object
gmaps = googlemaps.Client(key='INSERT YOUR API KEY HERE')

# call a method on the api
gmaps.reverse_geocode((latitude,longitude))

# find nearby places of interest
place = 'TYPE A PLACE'
gmaps.places(place, location=(latitude, longitude), radius=1000)


# json
import json

# The missing JSON inspector for chrome 
# https://chrome.google.com/webstore/detail/the-missing-json-inspecto/hhffklcokfpbcajebmnpijpkaeadlgfn
address = 'TYPE AN ADDRESS HERE'
api_json_url = r'https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(address)
r = requests.get(api_json_url)

# get the latitude and longitude from json
