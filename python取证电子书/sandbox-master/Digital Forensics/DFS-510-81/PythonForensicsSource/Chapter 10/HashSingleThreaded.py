# Single Threaded File Hasher

import hashlib
import os
import sys
import time

# Create a constant for the local directory
HASHDIR = 'c:\\HASHTEST\\'
# Create an empty list to hold the resulting hash results
results = []

try:
    # Obtain the list of files in the HASHDIR
    listOfFiles = os.listdir(HASHDIR)
    
    # Mark the starting time of the main loop
    startTime = time.time()  
    
    for eachFile in listOfFiles:
        # Attempt File Open
        fp = open(HASHDIR+eachFile, 'rb')
        # Then Read the contents into a buffer
        fileContents = fp.read()
        # Close the File 
        fp.close()
        # Create a hasher object of type sha256
        hasher = hashlib.sha256()
        # Hash the contents of the buffer
        hasher.update(fileContents)
        # Store the results in the results list
        results.append([eachFile, hasher.hexdigest()])
        # delete the hasher object
        del hasher
    
    # Once all the files have been hash calculate
    # the elapsed time
    
    elapsedTime = time.time() - startTime
    
except:
    # If any exceptions occur notify the user and exit
    print('File Processing Error')
    sys.exit(0)
    
# Print out the results
# Elapsed Time in Seconds and the Filename / Hash Results

print('Elapsed Time: ', elapsedTime, 'Seconds')
for eachItem in results:
    print eachItem

        
        