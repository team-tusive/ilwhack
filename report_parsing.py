# -*- coding: cp1252 -*-

#http://www.lbp.police.uk/information/latest_news/news_archives/2013/february-1.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives/2013.aspx
#http://www.lbp.police.uk/information/latest_news/news_archives.aspx

import urllib2
import time

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',\
                   'Accept-Language': 'en-us',\
                   'Accept-Encoding': '',\
                   'Keep-Alive': '300',\
                   'Connection': 'keep-alive',\
                   'Cache-Control': 'max-age=0'}
DEFAULT_LOCATION = 'Edinburgh'

s1 = '''Lothian and Borders Police are appealing for witnesses following a report of indecent exposure in Edinburgh.

The incident happened around 7.50pm on Tuesday 5 February, in the Leith area of the city.

A 33-year-old woman was walking home and reached the crossroads of Iona Street and Dickson Street when a man approached her before exposing himself.

The suspect then made off towards Easter Road where he was lost to sight. The victim returned home and contacted police.

Officers are now urging anyone who can assist with their enquiries to contact police immediately.

The suspect is described as white, around 5ft 6ins tall with an average build, fresh-faced and clean-shaven complexion. He was wearing a dark hooded top with yellow writing on the chest, grey jogging bottoms, a black shoulder bag and spoke with a Scottish accent.

A police spokesperson said: "The suspect exposed himself to the woman and made an inappropriate remark before running off.

"While she was uninjured, the victim was understandably distressed and we are keen to hear from anyone who remembers seeing anything suspicious in or around Iona Street on Tuesday evening.

"Similarly, anyone who recognises the description of the suspect is also asked to come forward."

Those with information can contact Lothian and Borders Police on 0131 311 3131, or the charity Crimestoppers in complete anonymity on 0800 555 111.'''

s2 = '''Lothian and Borders Police are appealing for witnesses after an elderly woman was assaulted and robbed in Edinburgh.

The 81-year-old was walking in Wester Hailes Road towards the Wester Hailes Plaza at around 7pm yesterday and began climbing the stairs of the footbridge.

At this time a male youth approached her and grabbed at her handbag and a carrier bag she was holding.

As a result of the struggle the victim fell down a number of stairs and injured her arm and shoulder.

The suspect then made off with the woman's bags and was pursued by a member of the public before being lost to sight.

A man, who was with his young daughter, then helped the victim to her feet and she returned home before contacting police and attending at hospital where she continues to be treated.

Police are now urging anyone who can assist with their enquiries to come forward.

The first suspect is described as white, 16 or 17-years-old and wearing a light coloured two-tone hooded top, light coloured jogging bottoms and trainers.

A police spokesman said: "As well as being extremely upset by the theft of her bags, the elderly woman also suffered a painful injury to her arm and shoulder, which required treatment.

"Anyone who was in the Wester Hailes Road area yesterday evening and remembers seeing anything suspicious is asked to contact police immediately.

"We are particularly keen to trace the member of the public who helped the victim up after her fall and would ask him to get in touch as soon as possible."

Those with information can contact Lothian and Borders Police on 0131 311 3131, or the charity Crimestoppers in complete anonymity on 0800 555 111.'''

s3 = '''Police in East Lothian are appealing for witnesses following a bogus caller incident in Port Seton on Tuesday, 5 February.

The suspect walked into the address in Inglis Avenue without invitation and claimed that he was there to fix the homeowner's satellite television system.

He then examined the satellite box, appearing to fumble with the cables, before demanding the owner pay £30 for his services.

The suspect produced what appeared to be a chip and pin device, and asked the owner to enter his bank card and supply his pin number. The owner refused, and the suspect left the house empty-handed.

He is described as white, in his 20s, 5ft 8ins tall, slim build, dark clothing, with a Fife accent.

A Lothian and Borders Police spokesman said: "We are appealing to anyone in the Port Seton area who received any kind of unsolicited visit by a man claiming to be there to check their satellite system, or carry out any kind of electrical or maintenance work, to contact police.

"Similarly, anyone who noticed a man matching the description of the suspect in Inglis Avenue or elsewhere in the local area should also get in touch.

"At this time we are warning residents to be mindful of the dangers posed by bogus callers.

"Anyone who receives an unsolicited call at their home by anyone offering to carry out maintenance or any other kind of work should deny them entry.

"If they claim to be from a utilities company then residents should check their identification, and if still in doubt, contact the company they claim to represent.

"If residents are suspicious as to the intentions of any cold caller then they should contact the police."

Anyone with any information should contact Lothian and Borders Police on 0131 311 3131, or Crimestoppers, where information can be reported anonymously, on 0800 555 111.'''

def url_request(url):
    txdata = None
    txheaders = DEFAULT_HEADERS
    request = urllib2.Request(url, txdata, txheaders)
    data = urllib2.urlopen(request).read()
    return data

class Incident(object):
	def __init__(self,url):
		self.url = url
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
		self.download_html()
		self.populate_data()
		if self.full_location != ', ' and self.full_location != None:
			self.viable = True
			#attempt to get coords here, set viable to false if coords fail?
	def download_html(self):
		self.raw_html = url_request(self.url)
	def populate_data(self):
		self.report = get_report(self.raw_html)
		self.plaintext_location = get_report_location(self.report)
		self.street_location = self.plaintext_location
		self.datetime = get_timedate(self.raw_html)
		self.title = get_title(self.raw_html)
		try:
			self.crimetype, self.general_location = self.title.split(', ')
			self.full_location = ', '.join([self.street_location,self.general_location])
		except ValueError: #title not of format "crimetype, location"
			if DEFAULT_LOCATION:
				self.full_location = ', '.join([self.street_location,DEFAULT_LOCATION])


road_names = ['avenue','street','road','estate','lane']
incident_exclusion_list = ['charged','arrested','arrest','arrests','appeal','update','?']

get_street_locations = lambda split_report: filter(lambda (x,y): y.lower() in road_names and y.istitle(),enumerate(split_report))

explode_report = lambda report: filter(lambda x: len(x)>0, report.replace('\n',' ').split(' '))

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
		if nextword.istitle() and nextword.lower() in road_names:
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
	timedate = time.strptime(raw_html, "%d %B %Y %H:%M") #day (00-31), month (full), year (full), hour(00-23), : minute
	return timedate #returns a struct_time http://docs.python.org/2/library/time.html#time.struct_time

def get_title(raw_html):
	start_title_tag = "<title>"
	end_title_tag = end_tag(start_title_tag)
	if start_title_tag not in raw_html:
		return None
	raw_html = raw_html[raw_html.find(start_title_tag)+len(start_title_tag):]
	raw_html = raw_html[:raw_html.find(end_title_tag)]
	return raw_html.replace('\n','').replace('\r','').replace('\t','')