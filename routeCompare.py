import urllib2
import json
import re

def testRoute(origin, destination):

   url = "http://maps.googleapis.com/maps/api/directions/json?mode=walking&sensor=false&alternatives=true&origin=" + "+".join(re.split(" +", origin)) + "&destination=" + "+".join(re.split(" +", destination))
   
   response = urllib2.urlopen(url)
   data = json.load(response)

   if data['status']!='OK':
      raise Exception("Unexpected status returned: " + data['status'])

   regex = ur"<b>[0-9]?/?([A-Z].+?)</b>+?"
   for route in data['routes']:
      print "------------------\n"
      for step in route['legs'][0]['steps']:
#         print step['html_instructions']
         if len(re.findall(regex, step['html_instructions']))>0:
            print re.findall(regex, step['html_instructions'])[0]
