# -*- coding: cp1252 -*-

#http://www.lbp.police.uk/information/latest_news/news_archives/2013/february-1.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives/2013.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives.aspx

# archive_url = 'http://www.lbp.police.uk/information/latest_news/news_archives.aspx'		 
# archives_2011 = 'http://www.lbp.police.uk/information/latest_news/news_archives/2011.aspx'
# archives_2012 = 'http://www.lbp.police.uk/information/latest_news/news_archives/2012.aspx'
# archives_2013 = 'http://www.lbp.police.uk/information/latest_news/news_archives/2013.aspx'
# archives_jan_2011 = 'http://www.lbp.police.uk/information/latest_news/news_archives/2011/january_2011.aspx'
# archives_feb_2012 = 'http://www.lbp.police.uk/information/latest\%20news/news\%20archives/2012/february\%202012.aspx'

import urllib2
import time
import getLocation
import traceback
import sys
import re

global debug_incident
debug_incident = None

SITE_URL = 'http://www.lbp.police.uk'

MONTHS = ['january','february','march','april','may','june','july','august',\
			'september','october','november','december']


fillable_archive_url = lambda month, year:\
		 SITE_URL + "/information/latest_news/news_archives/%s/%s_%s.aspx" %(year,month,year)

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',\
                   'Accept-Language': 'en-us',\
                   'Accept-Encoding': '',\
                   'Keep-Alive': '300',\
                   'Connection': 'keep-alive',\
                   'Cache-Control': 'max-age=0'}
DEFAULT_LOCATION = 'Edinburgh'

def url_request(url):
    txdata = None
    txheaders = DEFAULT_HEADERS
    request = urllib2.Request(url, txdata, txheaders)
    data = urllib2.urlopen(request).read()
    return data

def get_archive_page(month,year):
	if not 2011 <= year <= 2013:
		raise ValueError("Illegal year: " + year)
	if not month in MONTHS:
		raise ValueError("Illegal month: " + month)
	url = fillable_archive_url(month,str(year))
	if year == 2012 and MONTHS.index(month) < MONTHS.index('june'): #fuck you
		url = url.replace('_','%20') # fucking dumb fucking replacement of underscores with spaces for 2012 only. wtf lothian police???
	if year == 2012: #not even worth trying:
		if month == 'august':
			url = 'http://www.lbp.police.uk/information/latest_news/news_archives/2012/aug_2012.aspx'
		elif month == 'september':
			url = 'http://www.lbp.police.uk/information/latest_news/news_archives/2012/sept_2012.aspx'
		elif month == 'december':
			url = 'http://www.lbp.police.uk/information/latest%20news/news%20archives/2012/december%202012.aspx'
	if year == 2013:
		if month == 'january':
			url = url.replace('_2013','')
		if month == 'february':
			url = url.replace('_2013','-1') #???????? fuck whoever made this
	return url_request(url)

def get_incident_urls(raw_html):
	start_title_tag = '<table summary="box">'
	end_title_tag = "</table>"
	if start_title_tag not in raw_html:
		return None
	raw_html = raw_html[raw_html.find(start_title_tag)+len(start_title_tag):]
	raw_html = raw_html[:raw_html.find(end_title_tag)]
	link_starts = raw_html.split('''<a " href="''')
	link_starts = link_starts[1:] #first is gibberish
	links = [SITE_URL + link[:link.find('"')] for link in link_starts]
	return links

def isurl(input):
    return re.match("http",input)


class Incident(object):
	def __init__(self,inpt):
		self.error404 = False
		self.viable = False
		self.raw_html = None
		self.report = None
		self.datetime = None
		self.crimetype = None
		self.street_location = None
		self.general_location = None
		self.title = None
		self.full_location = None
		self.coords = (None,None)
		if isurl(inpt):
			self.url = inpt
			self.download_html()
		else:
			self.url = None
			try:
				self.raw_html = open(inpt,'r').read()
			except IOError as e:
				print e.message
		self.populate_data()
		if self.full_location != ', ' and self.full_location != None:
			self.viable = True
			try:
				print "\t\tLocation: " + str(self.full_location)
				print "\t\tGetLocation: " + str(getLocation.getLocation(str(self.full_location)))
				self.coords = getLocation.getLocation(str(self.full_location))
			except Exception as e:
				print e.message
				if "concatenate" in e.message:
					global debug_incident
					debug_incident = self
					traceback.print_exc(file=sys.stdout)
				self.viable = False                
                
	def download_html(self):
		try:
			self.raw_html = url_request(self.url)
		except urllib2.HTTPError as e:
			self.error404 = True
			self.errortext = e.message
	def populate_data(self):
		self.report = get_report(self.raw_html)
		self.plaintext_location = get_report_location(self.report)
		self.street_location = self.plaintext_location
		self.datetime = get_timedate(self.raw_html)
		self.title = get_title(self.raw_html)
		try:
			self.crimetype, self.general_location = self.title.split(', ')
			if not self.general_location.istitle():
				self.full_location = ', '.join([self.street_location,DEFAULT_LOCATION])
			else:
				self.full_location = ', '.join([self.street_location,self.general_location])
		except ValueError: #title not of format "crimetype, location"
			if DEFAULT_LOCATION and self.street_location:
				self.full_location = ', '.join([self.street_location,DEFAULT_LOCATION]).replace(',,',',')
		except TypeError:
			self.full_locations = None
	def tostring(self):
		try: 
			d = dict()
			d['full_location'] = self.full_location
			d['coords'] = str(self.coords)
			d['title'] = self.title
			d['crimetype'] = self.crimetype
			d['datetime'] = time.mktime(self.datetime)
			d['url'] = self.url
			return str(d).replace("u'","'")
		except: #some occasional errors with time.mktime: 
			return ""

road_names = ['avenue','street','road','estate','lane']
road_names += map(str.lower,['Gardens', 'End', 'Rigg', 'road', 'Way', 'SQ', 'Steps', 'Craigour', 'park', \
    'Ratho', 'Crammond', 'grove', 'Cross', 'terrace', 'Crescent', 'Wharf', 'Terrace', \
    'Terr', 'Comiston', 'Pend', 'Grange', 'Fountainbridge', 'Newbridge', 'View', 'Gait', 'Shaw', 'Lane', \
    'Queensferry', 'Medway', 'Brae', 'Rd', 'Causeway', 'Maybury', 'Loan', 'Wynd', 'gardens', 'Medway', 'raod', \
    'Crest', 'Row', 'Drive', 'Crecent', 'Hill', 'Place', 'hermitage', 'Steil', 'lane', 'Bow', 'S.Queensferry', \
    'Station', 'House', 'Kirkliston', 'Dykes', 'Yards', 'Circus', 'Lade', 'Bughtlinfield', 'drive', 'Links', \
    'Pl', 'Gdns', 'Grove', 'Balerno', 'Bank', 'Neuk', 'G', 'Glebe', 'Dr', 'Drylaw', 'La', 'Avenue', 'Port', 'Green', \
    'Close', 'Village', 'Square', 'Breakwater', 'Haugh', 'Road', 'Cres', 'Avenue', 'Werberside', 'Street', 'Ferry', 'Park', \
    'crescent', 'Joppa', 'Rise', 'Hermiston', 'Walk', 'L'])
#^ taken from Egidijus' data (from council)
incident_exclusion_list = ['charged','arrested','arrest','arrests','appeal','update','?','recovered']

get_street_locations = lambda split_report: filter(lambda (x,y): re.sub('[^a-z]','',y.lower()) in road_names and y.istitle(),enumerate(split_report))

explode_report = lambda report: filter(lambda x: len(x)>0, re.split('\s+',report))


end_tag = lambda start_tag: start_tag[0] + '/' + start_tag[1:]

def get_report(raw_html):
	start_report_tag = '</h1>'
	end_report_tag = '</div>'
	if not start_report_tag in raw_html:
		return None
	raw_html = raw_html[raw_html.find(start_report_tag)+len(start_report_tag):]
	raw_html = raw_html[:raw_html.find(end_report_tag)]
	raw_html = raw_html.replace('<br />\n','\n')
	for tag in ['<p>','<span>','<br />']:
		raw_html = raw_html.replace(tag,' ')
		raw_html = raw_html.replace(end_tag(tag),' ')
	return raw_html

def get_report_location(report):
	report_words = explode_report(report)
	try:
		street_incidence_index = get_street_locations(report_words)[0][0]
	except IndexError:
		return None
	while True: #account for cases like "Queensferry Street Lane"
		nextword = report_words[street_incidence_index + 1]
		if nextword.istitle(): #changed from requiring trailing words to be in road_words
			street_incidence_index+=1
		else:
			break
	start_location_index = street_incidence_index
	while True: 
		prevword = report_words[start_location_index - 1]
		if prevword.istitle() or prevword.isdigit():
			start_location_index-=1
		else:
			break
	return ' '.join(report_words[start_location_index:street_incidence_index+1])

def get_timedate(raw_html):
	start_report_tag = '"Template_NewsDate1_lblDate" style="float:right">'
	if start_report_tag not in raw_html:
		return None
	end_report_tag = "</span>"
	raw_html = raw_html[raw_html.find(start_report_tag)+len(start_report_tag):]
	raw_html = raw_html[:raw_html.find(end_report_tag)]
	#http://docs.python.org/2/library/time.html#time.strptime
	if not raw_html:
		return None
	timedate = time.strptime(raw_html, "%d %B %Y %H:%M") #day (00-31), month (full), year (full), hour(00-23), : minute
	return timedate #returns a struct_time http://docs.python.org/2/library/time.html#time.struct_time

def get_title(raw_html):
	start_title_tag = "<title>"
	end_title_tag = end_tag(start_title_tag)
	if start_title_tag not in raw_html:
		return None
	raw_html = raw_html[raw_html.find(start_title_tag)+len(start_title_tag):]
	raw_html = raw_html[:raw_html.find(end_title_tag)]
	return re.sub('[\r\t\n]','',raw_html)
