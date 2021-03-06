from rateStreet import Results
import urllib2
import json
import re
from datastore_crimes import *

def getRoutes(origin, destination):

# Given origin and destination, returns a 2-tuple (routes, data)
# where data is original response and routes is a list of routes in 6-tuples of the form:
# (distance_text, distance_value, start_address, end_address, streets, route)
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
            try:
               deeds = db.GqlQuery("SELECT * "
                                   "FROM Deed_entry "
                                   "WHERE ANCESTOR IS :1 "
                                   "AND street = :2",
                                   deeds_data_key(), street)
               street_crimes = len([deed for deed in deeds])
            except:
               street_crimes = 0
            rating = 0 if ratings.getValue(street) == None else ratings.getValue(street)
            streets.append((street, (rating + street_crimes))) 
      streets = set(streets)
      routedata = (distance_text, distance_value, start_address, end_address, streets, route)
      routes.append(routedata)
   return routes

def filterRoutes(route_list):

# Takes routes (5-tuples), and returns list of EITHER one or two routes.
# If one route, it is both safest and shortest.
# If two routes, the first is safest, and the second is shortest.
   
   route_safeties = [sum(map(lambda x: x[1],route[4])) for route in route_list]
   safest_route = None
   safest_route_score = 9999999
   shortest_route = None
   shortest_route_distance = 9999999
   for i in range(len(route_list)):
      route = route_list[i]
      if route_safeties[i] < safest_route_score:
         safest_route_score = route_safeties[i]
         safest_route = route
      if route[1] < shortest_route_distance:
         shortest_route_distance = route[1]
         shortest_route = route
   if safest_route == shortest_route:
      return [safest_route]
   return [safest_route,shortest_route]

def getBestRoutes(origin, destination):
   routes = getRoutes(origin,destination)
   return filterRoutes(routes)
