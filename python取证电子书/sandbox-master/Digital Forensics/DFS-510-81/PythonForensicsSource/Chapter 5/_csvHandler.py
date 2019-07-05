
import csv   #Python Standard Library -  for csv files

# 
# Class: _CSVWriter 
#
# Desc: Handles all methods related to comma separated value operations
#
# Methods  constructor:     Initializes the CSV File
#                writeCVSRow:   Writes a single row to the csv file
#                writerClose:      Closes the CSV File

class _CSVWriter:

    def __init__(self, fileName):
        try:
            # create a writer object and then write the header row
            self.csvFile = open(fileName, 'wb')
            self.writer = csv.writer(self.csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            self.writer.writerow( ('Image Path', 'TimeStamp', 'Camera Make', 'Camera Model', 'Lat Ref', 'Latitude', 'Lon Ref','Longitude' ) )
        except:
            log.error('CSV File Failure')

    def writeCSVRow(self, fileName, timeStamp, CameraMake, CameraModel,latRef, latValue, lonRef, lonValue):
        latStr = '%.8f' %  latValue
        lonStr= '%.8f' %  lonValue
        self.writer.writerow( (fileName, timeStamp, CameraMake, CameraModel, latRef, latStr, lonRef, lonStr))

    def __del__(self):
        self.csvFile.close()
