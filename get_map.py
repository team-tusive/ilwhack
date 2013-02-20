import urllib2
import urllib
import cStringIO
import math
from PIL import Image
from scrape_police_data import read_heatmap_file

def fromIncidentFile(filename,width=500):
	'''Takes width, csv file of incident data (as generated by scrape_police_data).
	Width defaults to 500'''
	pass

def fromHeatmapFile(filename,width=500):
	params = tuple(read_heatmap_file(filename))
	return _requestMap(width,*params)

def fromIncidents(width=500,*args):
	'''Tales width, Incidents
	Width defaults to 500'''
	params = tuple([(incident.coords['lat'],incident.coords['lng']) for incident in filter(lambda x: x.coords != (None, None),args)])
	return _requestMap(width,*params)

def fromTuples(width=500,*args):
	'''Takes (lat,long) tuples
	Width defaults to 500'''
	return _requestMap(width,*args)

def _requestMap(width=500,*args):
	'''Takes width and (lat,long) tuples. 
	Width defaults to 500'''
	#paramstring = 'http://maps.googleapis.com/maps/api/staticmap?sensor=false&size=%s&visible=' %(str(size)[1:-1].replace(' ',''))
	size = (width,_get_height(width))
	paramstring = 'http://maps.googleapis.com/maps/api/staticmap?visible=STUFF_HERE&size=MORE_STUFF&sensor=false'
	paramstring = paramstring.replace(str(size[0]) + 'x' + str(size[1]))
	#example = "50,30%7C50.5,30.5"
	delimiter = '%7C'
	visible = delimiter.join([','.join(arg) for arg in args])
	#paramstring = urllib.quote(paramstring)
	#paramstring = paramstring.replace('-','%2D')
	paramstring = paramstring.replace('STUFF_HERE',visible)
	print "Getting map from: " + paramstring
	img = urllib2.urlopen(paramstring).read()
	img = Image.open(cStringIO.StringIO(img)).convert("RGB")
	return img

def _get_height(width,tuplelist):
	tuplelist = filter(lambda x: x != (), tuplelist)
	lats = [float(item[0]) for item in tuplelist]
	lngs = [float(item[1]) for item in tuplelist]
	latmin = min(lats)
	latmax = max(lats)
	lngmin = min(lats)
	lngmax = max(lats)
	latdelta = latmax - latmin
	lngdelta = lngmax - lngmin
	height = (latdelta / lngdelta) * width
	return math.ceil(height)
