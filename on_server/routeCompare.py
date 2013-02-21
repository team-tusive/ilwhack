from rateStreet import Results
import urllib2
import json
import re

def getRoutes(origin, destination):

# Given origin and destination, returns a 2-tuple (routes, data)
# where data is original response and routes is a list of routes in 5-tuples of the form:
# (distance_text, distance_value, start_address, end_address, streets)
# where "streets" is a set of 2-tuples (street, rating)
# rating can be integer 0-4 or None and is taken from edinburgh_data_normalised.csv

   url = "http://maps.googleapis.com/maps/api/directions/json?mode=walking&sensor=false&alternatives=true&origin=" + "+".join(re.split(" +", origin)) + "&destination=" + "+".join(re.split(" +", destination))
   
   response = urllib2.urlopen(url)
   data = json.load(response)

   if data['status'] != 'OK':
      raise Exception("Unexpected status returned: " + data['status'])

   regex = ur"<b>[0-9]?/?([A-Z].+?)(?:/[A-Z][0-9]+?)??</b>+?"

   routes = []
   ratings = Results()
   for route in data['routes']:
      distance_text = route['legs'][0]['distance']['text']
      distance_value = route['legs'][0]['distance']['value']
      start_address = route['legs'][0]['start_address']
      end_address = route['legs'][0]['end_address']
      streets = []
      for step in route['legs'][0]['steps']:
         if len(re.findall(regex, step['html_instructions']))>0:
            street = re.findall(regex, step['html_instructions'])[0]
            streets.append((street, ratings.getValue(street)))
      streets = set(streets)
      routedata = (distance_text, distance_value, start_address, end_address, streets)
      routes.append(routedata)
   return (routes, data)
