from rateStreet import Results
import urllib2
import json
import re

def testRoute(origin, destination):

   url = "http://maps.googleapis.com/maps/api/directions/json?mode=walking&sensor=false&alternatives=true&origin=" + "+".join(re.split(" +", origin)) + "&destination=" + "+".join(re.split(" +", destination))
   
   response = urllib2.urlopen(url)
   data = json.load(response)

   if data['status'] != 'OK':
      raise Exception("Unexpected status returned: " + data['status'])

   regex = ur"<b>[0-9]?/?([A-Z].+?)</b>+?"

   thestring = ""
   ratings = Results()
   for route in data['routes']:
      thestring += "------------------\n"
      streets = []
      for step in route['legs'][0]['steps']:
#        print step['html_instructions']
         if len(re.findall(regex, step['html_instructions']))>0:
            streets.append(re.findall(regex, step['html_instructions'])[0])
      streets = list(set(streets))
      for street in streets:
         rating = " None " if ratings.getValue(street) == None else " " + str(ratings.getValue(street)) + " "
         thestring += street + rating + "\n"
   return thestring
