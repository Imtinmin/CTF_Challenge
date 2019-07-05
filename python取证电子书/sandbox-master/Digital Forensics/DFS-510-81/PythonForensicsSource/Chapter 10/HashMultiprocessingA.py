# Multiprocessing File Hasher A

import hashlib
import os
import sys
import time
import multiprocessing


# Create a constant for the local directory
HASHDIR = 'c:\\HASHTEST\\'

#
# hashFile Function, designed for multiprocessing
# 
# Input: Full Pathname of the file to hash
#
# 

def hashFile(fileName):

    try:
        
        fp = open(fileName, 'rb')
        
        # Then Read the contents into a buffer
        fileContents = fp.read()
        
        # Close the File 
        fp.close()
        
        # Create a hasher object of type sha256
        hasher = hashlib.sha256()
        
        # Hash the contents of the buffer
        hasher.update(fileContents)
        
        print(fileName, hasher.hexdigest())
        
        # delete the hasher object
        del hasher
    
    except:
        # If any exceptions occur notify the user and exit
        print('File Processing Error')
        sys.exit(0)
        
    return True
  
#  
# Create Main Function
#

if __name__ == '__main__':
    
    # Obtain the list of files in the HASHDIR
    listOfFiles = os.listdir(HASHDIR)
    
    # Mark the starting time of the main loop
    startTime = time.time()  
    
    #create 4 sub-processes to do the work (one of each core in this test)
    
    # Each Process contains:
    #              Target function hashFile() it this example
    #              Filename: picked from the list generate by os.listdir()    
    #                        once again an instance of the same 249MB file is used
    #                    
    # Next then we start each of the processes
    
    coreOne = multiprocessing.Process(target=hashFile, args=(HASHDIR+listOfFiles[0],) )
    coreOne.start()
    
    coreTwo = multiprocessing.Process(target=hashFile, args=(HASHDIR+listOfFiles[1],) )
    coreTwo.start()
    
    coreThree = multiprocessing.Process(target=hashFile, args=(HASHDIR+listOfFiles[2],) )
    coreThree.start()
    
    coreFour = multiprocessing.Process(target=hashFile, args=(HASHDIR+listOfFiles[3],) )
    coreFour.start()
    
    # Next we use the join to wait for all processes to complete
    
    coreOne.join()
    coreTwo.join()
    coreThree.join()
    coreFour.join()
    
    # Once all the files have been hashed and results printed
    # I calculate the elapsed time
    
    elapsedTime = time.time() - startTime
    
    print('Elapsed Time: ', elapsedTime, 'Seconds')


        
        