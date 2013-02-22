import urllib2
import json
import re

def getLocation(location):
   "Given a string with a street name, this function returns a location or an error"

   # build the url we will use to query googles API. We join the tokens in the location string with plusses, e.g. "Royal+Mile+Edinburgh"
   url = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='+"+".join(re.split(" +", location))
   
   #send query, get json, ???, profit!
   response = urllib2.urlopen(url)
   data = json.load(response)

   #if google reports an error, we propagate it to our caller
   if data['status']!='OK':
      raise Exception("Unexpected status returned: " + str(data['status']))

   #extract and return the given location to our caller.
   return data['results'][0]['geometry']['location']

def getName(coords):
   "Given a pair of GPS coordinates, this function returns a location name"

   # build the url we will use to query googles API. We join the tokens in the location string with plusses, e.g. "Royal+Mile+Edinburgh"
   url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%f,%f&sensor=false" % coords
   
   #send query, get json, ???, profit!
   response = urllib2.urlopen(url)
   data = json.load(response)

   #if google reports an error, we propagate it to our caller
   if data['status']!='OK':
      raise Exception("\tUnexpected status returned: " + str(data['status']))
   #Yay! regexp!
   return re.sub(",.*","",re.sub("^[^a-zA-Z]*","",data['results'][0]['formatted_address']))

   

