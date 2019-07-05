# MultiCore Password Table Generator

# import standard libraries

import hashlib              # Hashing the results
import time                 # Timing the operation
import os
import itertools            # Creating controled combinations
import multiprocessing      # Multiprocessing Library

#
# Create a list of characters to include in the
# password generation
#

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Define a hypothetical SALT value
SALT = "&45Bvx9"

# Define the allowable range of password length

PW_LOW  = 4
PW_HIGH = 8    


def pwGenerator(size):

    pwCount = 0
    # create a loop to include all passwords
    # within range specified

    try:
        
        # Open a File for writing the results
        fp = open('PW-'+str(size), 'w')
        
        for r in range(size, size+1):
    
            #Apply the standard library interator
     
            for s in itertools.product(chars, repeat=r):
                # Process each password as they are
                # generated
                pw = ''.join(s)

                # Perform hashing of the password
                md5Hash = hashlib.md5()
                md5Hash.update(SALT+pw)
                md5Digest = md5Hash.hexdigest()
                
                # Write the hash, password pair to the file
                fp.write(md5Digest + ' ' + pw + '\n')
                pwCount += 1
                del md5Hash
                
    except:
        print 'File/Hash Processing Error'    
    finally:
            fp.close()
            print str(size),' Passwords Processed= ', pwCount

#  
# Create Main Function
#

if __name__ == '__main__':

    print 'Processing Multi Core'
    print os.getcwd()
    print 'Password string: ', chars    
    print 'Password Lenghts: ', str(PW_LOW), ' - ', str(PW_HIGH)

    # Mark the starting time of the main loop
    startTime = time.time()  

    #create a process Pool with 5 processes
    corePool = multiprocessing.Pool(processes=5)

    #map corePool to the Pool processes
    results = corePool.map(pwGenerator, (4, 5, 6, 7, 8))
    
    elapsedTime = time.time() - startTime            

    # When complete calculate the elapsed time
    
    elapsedTime = time.time() - startTime   
    print 'Multi Core Rainbow Complete'
    print 'Elapsed Time: ', elapsedTime
    #print 'Passwords Generated: ', pwCount
    print