import datetime
import csv
import getLocation
import math

class Crime:
    def __init__(self,crimetype,title,url,datet,coords,location,streetname):
        self.crimetype = crimetype
        self.title = title
        self.url = url
        self.unixtime = datet
        self.datet = datetime.datetime.fromtimestamp(int(datet)).strftime('%Y-%m-%d %H:%M:%S')
        self.hour = self.datet[-8:-6]
        self.coords = coords
        self.street = streetname
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
    def getLocationnonUrl(self):
        return self.location
    def getCoords(self):
        return self.coords


class Crimes:

    def __init__(self,datapath,typepath, optionalCsvStreetNameCoordinate):
        temp_data = open(datapath,'r')
        data = temp_data.read()
        self.streetscoord = list()
        tempdata = open(optionalCsvStreetNameCoordinate).read()
        
        while (tempdata.find("\n")!=-1):
            elem = tempdata[:tempdata.find("\n")]
            x = tempdata[:tempdata.find("\t")]
            tempdata = tempdata[tempdata.find("\t")+1:]
            y = tempdata[:tempdata.find("\t")]
            tempdata = tempdata[tempdata.find("\t")+1:]
            streettmp = tempdata[:tempdata.find("\n")]
            tempdata = tempdata[tempdata.find("\n")+1:]
            item=((x,y),streettmp)
            self.streetscoord.append(item)

            
        type_data = csv.reader(open(typepath,'r'))
        self.types = list()
        for row in type_data:
            for item in row:
                self.types.append(item)
        self.result = list()
        while (data.find(",\n,\n" )!= (-1)):
            data=data.replace(",\n,\n",",\n")
        
        while (data.find("}") != (-1)):
            if data.find("\n") != (-1):
                tempdata = self.toCrime(data[data.find("{")+1:data.find("\n")],self.streetscoord)
                if tempdata!=None:
                    self.result.append(tempdata)
                data = data[data.find("\n")+1:]
            else:
                tempdata =self.toCrime(data,self.streetscoord)
                if tempdata != None:
                    self.result.append(tempdata)
                data = ""
        #fileout = open("output.csv",'w')
        #out = ""
       # for item in self.streetscoord:
        #    out+= str(item[0][0]) +'\t'+str(item[0][1])+'\t'+str(item[1])+'\n'
       # fileout.write(out)
       # fileout.close()
    def printCrimeData(self):
        fileout = open("usefuldata.csv",'w')
        out = ""
        for crime in self.result:
            coords = crime.coords
            lat = coords[0][1:]
            lon = coords[1][1:]
            out += '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(crime.title, crime.crimetype, crime.hour, lat, lon, crime.street)
        fileout.write(out)
        fileout.close()


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
    

        

    def toCrime (self,data,streetscoordtmp):
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

            street = None
            if ('none'.lower() not in coords[0].lower()):
                for streetname in self.streetscoord: 
                    if (round(float(coords[0]),7),round(float(coords[1]),7)) == (round(float(streetname[0][0]),7),round(float(streetname[0][1]),7)):
                        street = streetname[1]
#                        print("found")
                        break
                if street== None:
                    print("search")
                    street = str(getLocation.getName((float(coords[0]),float(coords[1]))))
                    self.streetscoord.append(((float(coords[0]),float(coords[1])),street))
                    

            
            if 'none' in crimetype.lower():
                for item in self.types:
                    if item.lower() in title.lower():
                            crimetype = item
                            break
            if (coords!= ["None","None"]) :
                if ( (math.sqrt((float(coordx)-55.954198)**2+(float(coordy) + 3.188782)**2)<2)):     
                    return Crime(crimetype,title,url,datetimesec,coords,location,street)
                return None
        except:
                return None
        
