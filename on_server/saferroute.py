from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from routeCompare import testRoute
import urllib2
import json
import re

class MainPage(webapp.RequestHandler):
   def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write("testRoute('Edinburgh', 'Glasgow')\n")
      self.response.out.write(testRoute('Edinburgh', 'Glasgow'))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                      debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
   main()
