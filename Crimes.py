import datetime
import csv

class Crime:
    def __init__(self,crimetype,title,url,datet,coords,location):
        self.crimetype = crimetype
        self.title = title
        self.url = url
        self.datet = datetime.datetime.fromtimestamp(int(datet)).strftime('%Y-%m-%d %H:%M:%S')
        self.coords = coords
        self.location = location
        self.datesec = datet % 86400

     
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
    def getLocation(self):
        return self.location
    def getCoords(self):
        return self.coords


class Crimes:

    def __init__(self,datapath,typepath):
        temp_data = open(datapath,'r')
        data = temp_data.read()
        type_data = csv.reader(open(typepath,'r'))
        self.types = list()
        for row in type_data:
            for item in row:
                self.types.append(item)
        self.result = list()    
        while (data.find("}")!=(-1)):
            if data.find("\n")!= (-1):
                self.result.append(self.toCrime(data[data.find("{")+1:data.find("\n")]))
                data = data[data.find("\n")+1:]
            else:
                self.result.append(self.toCrime(data))
                data = ""

    
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
    

    def toCrime (self,data):
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
        return Crime(crimetype,title,url,datetimesec,coords,location)
        