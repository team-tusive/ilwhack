import urllib2
import json
import re

def getLocation(location):
   "Given a string with a street name, this function returns a location ar an error"

   # build the url we will use to query googles API. We join the tokens in the location string with plusses, e.g. "Royal+Mile+Edinburgh"
   url = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='+"+".join(re.split(" +", location))
   
   #send query, get json, ???, profit!
   response = urllib2.urlopen(url)
   data = json.load(response)

   #if google reports an error, we propagate it to our caller
   if data['status']!='OK':
      raise Exception("Unexpected status returned: " + str(data['status']))

   #if we get several results, we can't determine what our caller wants, so we raise an exception.
   if len(data['results'])>1:
      raise Exception("Ambigous result returned: " + str(data['results']))
   #we know that results contains exactly one entry (since status != OK if we don't get any results)
   #extract and return the given location to our caller.
   return data['results'][0]['geometry']['location']
