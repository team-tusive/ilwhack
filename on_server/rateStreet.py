import csv

class Results:

    def __init__(self):    
        self.reader = csv.reader(open('edinburgh_data_normalised.csv', 'r'), delimiter=',')
        self.ratings = dict()
        for row in self.reader:
            if  len(row[6])==1:
                if (row[1].lower() not in self.ratings):
                    self.ratings[row[1].lower()] = ((ord(row[6]) - 64)) * 0.2
                else:
                    self.ratings[row[1].lower()] = (max((ord(row[6]) -64),self.ratings[row[1].lower()]) * 0.2)
#        print(self.ratings)

    def getValue(self, streetName):
        if streetName.lower() not in self.ratings:
            return None
        return self.ratings[streetName.lower()]
