#
# GPS Extraction
# Python-Forensics
# No HASP required

# Revision 1.2
#
# Added module pfGoogle that automatically generates an html file
# that includes all the gps points as an output file: ./pfmap.html
# Opening that fill will display a zoomabl world map with picture points
# In addition, the name of the file associated with the point is available
# when mousing over the point.
#
# Note: To use the latest version you must install the following 3rd party packages
#
# 1) pfGoogle
# 2) Pillow  i.e. pip install Pillow
#

import os                               # Python Standard Library: OS Methods
import _modEXIF                         # EXIF Extraction Module
import _csvHandler                      # CSV Handler
import _commandParser                   # Command Parser
from classLogging import _ForensicLog   # Class Logging
import pfGoogle                         # New pfGoogle Interface Module

# Offsets into the return exifData for
# TimeStamp, Camera Make and Model

TS = 0
MAKE = 1
MODEL = 2

# Process the Command Line Arguments
userArgs = _commandParser.ParseCommandLine()

# create a log object
logPath = userArgs.logPath+"ForensicLog.txt"
oLog = _ForensicLog(logPath)

oLog.writeLog("INFO", "Scan Started")

csvPath = userArgs.csvPath+"imageResults.csv"
oCSV = _csvHandler._CSVWriter(csvPath)

# define a directory to scan
scanDir = userArgs.scanPath
try:
    picts = os.listdir(scanDir)
except:
    oLog.writeLog("ERROR", "Invalid Directory "+ scanDir)
    exit(0)

print "Program Start"
print

# CDH
# Created a mapping object

mymap = pfGoogle.maps(33.7167, 78.8833, 3)

for aFile in picts:
    
    targetFile = scanDir+aFile
    
    if os.path.isfile(targetFile):

        gpsDictionary, exifList = _modEXIF.ExtractGPSDictionary(targetFile)

        if (gpsDictionary != None):

            # Obtain the Lat Lon values from the gpsDictionary
            # Converted to degrees
            # The return value is a dictionary key value pairs
            
            dCoor = _modEXIF.ExtractLatLon(gpsDictionary)

            if dCoor:
                lat = dCoor.get("Lat")
                latRef = dCoor.get("LatRef")
                lon = dCoor.get("Lon")
                lonRef = dCoor.get("LonRef")
                
                if ( lat and lon and latRef and lonRef):
                    print str(lat)+','+str(lon)
                    
                    # CDH Place Points on the Map
                    mymap.addpointwithTitle(lat, lon, "#0000FF",aFile)
                    
                    # write one row to the output file         
                    oCSV.writeCSVRow(targetFile, exifList[TS], exifList[MAKE], exifList[MODEL],latRef, lat, lonRef, lon)
                    oLog.writeLog("INFO", "GPS Data Calculated for :" + targetFile)
                else:
                    oLog.writeLog("WARNING", "No GPS EXIF Data for "+ targetFile)
            else:
                oLog.writeLog("WARNING", "Improper GPS Data for "+targetFile)
        else:
            oLog.writeLog("WARNING", "No GPS EXIF Data for "+ targetFile)
    else:
        oLog.writeLog("WARNING", targetFile + " not a valid file")

print "Program End"

# Create the file containing the Google Map
mymap.draw('./pfmap.html')

# Clean up and Close Log and CSV File        
del oLog
del oCSV
        
