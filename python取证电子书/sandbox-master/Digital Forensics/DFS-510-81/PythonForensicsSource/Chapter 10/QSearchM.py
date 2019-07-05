# Simple Files Search Single Core Processing

keywords = ["hacker", "hacking", "2600", "password", "key", "heartbeat", "hook"]

import time

def SearchFile(theFile, theString):
    try:
        fp = open(theFile,'r')
        buffer = fp.read()
        fp.close()
        if theString in buffer:
            print 'File: ', theFile, ' String: ', theString, '\t', ' Found'
        else:
            print 'File: ', theFile, ' String: ', theString, '\t', ' Not Found'  
    except:
        print 'File processing error'

startTime = time.time()

SearchFile('c:\\TESTDIR\\Dictionary.txt', 'thought')
SearchFile('c:\\TESTDIR\\Dictionary.txt', 'exile')
SearchFile('c:\\TESTDIR\\Dictionary.txt', 'xavier')
SearchFile('c:\\TESTDIR\\Dictionary.txt', '$Slllb!')

elapsedTime = time.time() - startTime
print 'Duration: ', elapsedTime, ' Seconds'




    