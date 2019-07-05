# 
# p-search : Python Word Search
# Author: C. Hosmer
# August 2013
# Version 1.0
#
# Simple p-search python program
#
# Read in a list of search words
# Read a binary file into a bytearray
# Search the bytearray for occurances of any specified search words
# Print a HEX/ ASCII display localizing the matching words
# Print out a list of possible words identified that didn't match
#
# Definition of a word.  a word for this example is an uninterrupted sequence of 
# 4 to 12 alpha characters 
#

import logging
import time
import _psearch

if __name__ == '__main__':

    PSEARCH_VERSION = '1.0'
       
    # Turn on Logging
    logging.basicConfig(filename='pSearchLog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

    # Process the Command Line Arguments
    _psearch.ParseCommandLine()
   
    log = logging.getLogger('main._psearch')
    log.info("p-search started")

    # Record the Starting Time
    startTime = time.time()
    
    # Perform Keyword Search
    _psearch.SearchWords()
    
    # Record the Ending Time
    endTime = time.time()    
    duration = endTime - startTime   
    
    logging.info('Elapsed Time: ' + str(duration) + ' seconds')
    logging.info('')
    logging.info('Program Terminated Normally')

    
    
    


   

        






