import os
import urllib2
import json
import re
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from routeCompare import getRoutes


class GetRoutes(webapp.RequestHandler):
   def post(self):
      origin = cgi.escape(self.request.get('origin'))
      destination = cgi.escape(self.request.get('destination'))
      routes = getRoutes(origin, destination)

      template_values = {
         'routes': routes
      }
      path = os.path.join(os.path.dirname(__file__), 'templates/result.html')
      self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication(
                                     [('/search', GetRoutes)],
                                      debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
   main()
