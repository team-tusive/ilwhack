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
      routes,result = getBestRoutes(origin, destination)

      template_values = {
         'routes': routes,
         'result': json.dumps(result, separators=(',',':'))
      }
      path = os.path.join(os.path.dirname(__file__), 'templates/result.html')
      self.response.out.write(template.render(path, template_values))

class GetApiResponse(webapp.RequestHandler):
   def get(self):
      hour = int(self.request.get('hour'))
      crimesService = Crimes()
      crimelist = crimesService.findWithinTime(hour, 0, 60)
      googlepoints = crimesService.crimelisttoGoogle(crimelist)
      self.response.headers.add_header('content-type', 'application/javascript', charset='utf-8')
      self.response.out.write(googlepoints)
#      data = {'key':'test value'}
#      dataSerialized = json.dumps(data)
#      self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
#      self.response.out.write(dataSerialized)


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
