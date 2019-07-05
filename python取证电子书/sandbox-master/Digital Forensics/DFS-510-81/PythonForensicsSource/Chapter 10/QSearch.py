# Simple Files Search Single Core Processing

import time
import os

def SearchFile(theFile):

    keywords = ["hacker", "hacking", "2600", "password", "key", "heartbeat", "hook"]

    try:
        print os.getcwd()
        fp = open(theFile,'r')
        buffer = fp.read()
        fp.close()
        for eachWord in keywords:
            cnt = buffer.count(eachWord)
            print 'File: ', theFile, 'Keyword: ', eachWord, '\t', ' Found:', str(cnt) 
    except:
        print 'File processing error'

startTime = time.time()

SearchFile('.\Files\hackingcorpus-01.txt')
SearchFile('.\\Files\\hackingcorpus-02.txt')
SearchFile('.\\Files\\hackingcorpus-03.txt')
SearchFile('.\\Files\\hackingcorpus-04.txt')

elapsedTime = time.time() - startTime

print 'Duration: ', elapsedTime, ' Seconds'




    