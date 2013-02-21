import datetime
import csv
import getLocation
import math

class Crime:
    def __init__(self,crimetype,title,url,datet,coords,location):
        self.crimetype = crimetype
        self.title = title
        self.url = url
        self.datet = datetime.datetime.fromtimestamp(int(datet)).strftime('%Y-%m-%d %H:%M:%S')
        self.coords = coords
        self.location = location
        self.datesec = datet % 86400
        if ('none'.lower() not in self.coords[0].lower()):
            self.street = str(getLocation.getName((float(self.coords[0]),float(self.coords[1]))))
        else:
            self.street = None
     
    def getDateTime(self):
        return self.datet
    def getTimeOnly(self):
        return self.datet[-8:-3]
    def getType(self):
        return self.crimetype
    def getMonth(self):
        return int(float(self.datet[5:7]))
    def getYear(self):
        return int(float(self.datet[:4]))
    def getTitle(self):
        return self.title
    def getUrl(self):
        return self.url
    def getLocationnonUrl(self):
        return self.location
    def getCoords(self):
        return self.coords


class Crimes:

    def __init__(self):
        temp_data = open('full_data.csv','r')#hardcoded
        data = temp_data.read()
        type_data = csv.reader(open('Crimes.types','r'))#hardcoded
        self.types = list()
        for row in type_data:
            for item in row:
                self.types.append(item)
        self.result = list()
        while (data.find(",\n,\n" )!= (-1)):
            data=data.replace(",\n,\n",",\n")
        
        while (data.find("}")!=(-1)):
            if data.find("\n")!= (-1):
                tempdata = self.toCrime(data[data.find("{")+1:data.find("\n")])
                if tempdata!=None:
                    self.result.append(tempdata)
                data = data[data.find("\n")+1:]
            else:
                tempdata =self.toCrime(data)
                if tempdata != None:
                    self.result.append(tempdata)
                data = ""

    def findofTypes (self, crimeTypes):
        finalres= list()
        for crimetype in crimeTypes:
            for crime in self.result:
               if (crimetype.lower() in crime.crimetype.lower()):
                    finalres.append(crime)
        return finalres

    
    def findWithinTime(self, targetTimeHour,targetTimeMinute, timeRangeMinutes):
       finalres= list()
       for crime in self.result:
            if ((crime.datesec >(targetTimeHour*3600+targetTimeMinute*60-timeRangeMinutes*60)) & (crime.datesec<(targetTimeHour*3600+targetTimeMinute*60+timeRangeMinutes*60))):
                finalres.append(crime)

       return finalres
    def findWithinDate(self,targetYear,targetMonth):
       finalres = list()
       for crime in self.result:
           if ((crime.getMonth()==int(float(targetMonth))) & (int(float(targetYear))== crime.getYear())):
               finalres.append(crime)
       return finalres
    
    def crimelisttoGoogle(self,listofCrimes):
        result="heatmapData = [\n"
        for crime in listofCrimes:
            if 'none' not in crime.coords[0].lower():
                result =result + "	new google.maps.LatLng(" + crime.coords[0]+", "+crime.coords[1]+"),\n"
        result = result+ "];"
        return result

    def streetCrimed(self, listofStreets):
        result = list()
        for street in listofStreets:
            tempres = 0
            for crime in self.result:
                if crime.street!=None:
                    if street.lower() in crime.street.lower():
                        tempres=tempres+1
            if tempres !=0:
                result.append((street,tempres))
        return result
    

        

    def toCrime (self,data):
        try:
            crimetype = data[data.find(":")+1:data.find(",")]
            data = data[data.find(",")+1:]
            data = data[data.find("'")+1:]
            data = data[data.find("'")+1:]
            data = data[data.find("'")+1:]
            title = data[:data.find("'")]
            data = data[data.find("'"):]
            data = data[data.find("'")+1:]
            data = data[data.find("'")+1:]
            data = data[data.find("'")+1:]
            data = data[data.find("'")+1:]    
            url = data[:data.find("'")]
            data = data[data.find("'"):]
            data = data[data.find(":")+2:]
            datetimesec = float(data[:data.find(",")])
            data = data[data.find(",")+1:]
            data = data[data.find(":")+1:]
            if (data.find("None)")!=-1):
                coords = ["None","None"]
            else:
                coordx = data[data.find(":")+1:data.find(",")]
                data = data[data.find(",")+1:]
                coordy = data[data.find(":")+1:data.find("}")]
                coords = [coordx,coordy]
            data = data[data.find("}")+1:]
            data = data[data.find(":")+1:]
            data = data[data.find("'")+1:]
            location = data[:data.find("'")]
            if 'none' in crimetype.lower():
                for item in self.types:
                    if item.lower() in title.lower():
                            crimetype = item
                            break
            if (coords!= ["None","None"]) :
                if ( (math.sqrt((float(coordx)-55.954198)**2+(float(coordy) + 3.188782)**2)<2)):     
                    return Crime(crimetype,title,url,datetimesec,coords,location)
                return None
        except:
            return None
        
