from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from routeCompare import testRoute
import urllib2
import json
import re
import cgi

class MainPage(webapp.RequestHandler):
   def get(self):
      self.response.headers['Content-Type'] = 'text/html'
      self.response.out.write("""
          <html>
            <body>
              <form action="/search" method="post">
                <div><input type="text" name="origin"><label for="origin">Origin</label></div>
                <div><input type="text" name="destination"><label for="destination">Destination</label></div>
                <div><input type="submit" value="Get Routes"></div>
              </form>
            </body>
          </html>""")

class GetRoutes(webapp.RequestHandler):
   def post(self):
      origin = cgi.escape(self.request.get('origin'))
      destination = cgi.escape(self.request.get('destination'))
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write("testRoute('" + origin + "', '" + destination + "')\n")
      self.response.out.write(testRoute(origin, destination))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/search', GetRoutes)],
                                      debug=True)

def main():
   run_wsgi_app(application)

if __name__ == "__main__":
   main()
