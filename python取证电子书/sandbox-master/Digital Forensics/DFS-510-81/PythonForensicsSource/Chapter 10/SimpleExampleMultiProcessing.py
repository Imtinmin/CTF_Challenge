# Simple Files Search MultiProcessing

from multiprocessing import Process
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

#  
# Create Main Function
#

if __name__ == '__main__':
    
    startTime = time.time()
    
    p1 = Process(target=SearchFile, args=('c:\\TESTDIR\\Dictionary.txt', 'thought') )
    p1.start()
    
    p2 = Process(target=SearchFile, args=('c:\\TESTDIR\\Dictionary.txt', 'exile')  )
    p2.start()
    
    p3 = Process(target=SearchFile, args=('c:\\TESTDIR\\Dictionary.txt', 'xavier')  )
    p3.start()
    
    p4 = Process(target=SearchFile, args=('c:\\TESTDIR\\Dictionary.txt', '$Slllb')  )
    p4.start()
    
    # Next we use the join to wait for all processes to complete
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    elapsedTime = time.time() - startTime
    print 'Duration: ', elapsedTime
    
# Program Output

