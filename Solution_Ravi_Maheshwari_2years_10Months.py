import csv
from collections import namedtuple
 
class Peak (namedtuple('Peak', ['year', 'month', 'price'])):
        def __lt__(self, current):
            #Lesser than(<) operator is overlodaed here
            return self.price is None or self.price < current.price
        def __eq__(self, current):
            #Equals to (==) operator is overlodaed here
            return self.price == current.price
        def __gt__(self, current):
            #Greater than(<) operator is overlodaed here
            return current.price is None or self.price > current.price
 
def GetMaxStockPrices(fileObject):
    csv_reader = csv.DictReader(fileObject)
    companies = csv_reader.fieldnames[2:]
    # First two columns are discard Year & Month
    GetMAX = dict((comp, Peak(None, None, None)) for comp in companies)
    for row in csv_reader:
        year, month = row['Year'], row['Month']#Get Year & Month value
        current = dict((comp, Peak(year, month, float(row[comp]))) for comp in companies)
        GetMAX = dict((comp, max(GetMAX [comp], current[comp])) for comp in companies)
    return GetMAX
 
def main():
    # Can take a input_csv importing modules
    with open('Share_Prices_List.csv') as fileObject:# File opened
        max = GetMaxStockPrices(fileObject) #Get list of required values of share
        for company in sorted(max):
            print("%s: %s %s (%.f)" % (company, max[company].year, max[company].month, max[company].price)) # Print all required values.
if __name__ == "__main__":
    main()  
