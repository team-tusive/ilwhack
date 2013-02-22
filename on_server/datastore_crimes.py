from google.appengine.ext import db

class Deed_entry(db.Model):
   title = db.StringProperty()
   crime_type = db.StringProperty()
   time = db.IntegerProperty()
   lat = db.StringProperty()
   lon = db.StringProperty()
   street = db.StringProperty()

#Witness appeal, Edinburgh	 'Witness appeal'	1311074040	55.953647599999996	-3.2853441999999999	Ransome Gardens
def deeds_data_key(deed_data_name=None):
   """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
   return db.Key.from_path('Deed_data', deed_data_name or 'default_deed_data')

def add_data():
   with open("usefuldata.csv") as infile:
      for line in infile:
         splitline = line.split("\t")
         deed = Deed_entry(parent=deeds_data_key())
         deed.title = splitline[0]
         deed.crime_type = splitline[1]
         deed.time = int(splitline[2])
         deed.lat = splitline[3]
         deed.lon = splitline[4]
         deed.street = splitline[5][:-1]
         deed.put()
