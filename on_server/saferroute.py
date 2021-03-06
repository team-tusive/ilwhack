import os
import urllib2
import json
import re
import cgi
import json
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from routeCompare import getBestRoutes
from Crimes import *
from datastore_crimes import *

class GetRoutes(webapp.RequestHandler):
   def post(self):
      origin = cgi.escape(self.request.get('origin'))
      destination = cgi.escape(self.request.get('destination'))
      routes = getBestRoutes(origin, destination)
      routesroutes = list()
      for route in routes:
         routesroutes.append(route[5])

      template_values = {
         'routes': routes,
         'result': json.dumps(routesroutes, separators=(',',':'))
      }
      path = os.path.join(os.path.dirname(__file__), 'templates/result.html')
      self.response.out.write(template.render(path, template_values))

class GetApiResponse(webapp.RequestHandler):
   def get(self):

      hour = self.request.get('hour')

      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')

      data = []
      if hour == 'all':
         deeds = db.GqlQuery("SELECT * "
                             "FROM Deed_entry "
                             "WHERE ANCESTOR IS :1 ",
                             deeds_data_key())
         for deed in deeds:
            dataobject = { 'crime_type' : deed.crime_type,
                           'lat' : deed.lat,
                           'lon' : deed.lon,
                           'street' : deed.street,
                           'time' : deed.time,
                           'title' : deed.title }
            data.append(dataobject)
      else:
         deeds = db.GqlQuery("SELECT * "
                             "FROM Deed_entry "
                             "WHERE ANCESTOR IS :1 "
                             "AND time = :2 ",
                             deeds_data_key(), int(hour))
         for deed in deeds:
            dataobject = { 'crime_type' : deed.crime_type,
                           'lat' : deed.lat,
                           'lon' : deed.lon,
                           'street' : deed.street,
                           'time' : deed.time,
                           'title' : deed.title }
            data.append(dataobject)

#      data = {'key':'test value'}
      dataSerialized = json.dumps(data)
#      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
      self.response.out.write(dataSerialized)


class DataSt(webapp.RequestHandler):
#temporary just to load data into datastore
   def get(self):
      add_data()
      self.response.headers.add_header('content-type', 'text/plain', charset='utf-8')
      deeds = db.GqlQuery("SELECT * "
                          "FROM Deed_entry "
                          "WHERE ANCESTOR IS :1 ",
                          deeds_data_key())
      for a in deeds:
         self.response.out.write(a.street + " " + a.lat)


application = webapp.WSGIApplication(
                                     [('/search', GetRoutes),
                                      ('/api', GetApiResponse),
                                      ('/datastore', DataSt)],
                                      debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
   main()
