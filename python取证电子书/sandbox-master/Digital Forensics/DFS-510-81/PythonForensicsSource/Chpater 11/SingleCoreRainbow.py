# Single Core Password Table Generator

# import standard libraries

import hashlib              # Hashing the results
import time                 # Timing the operation
import sys
import os
import itertools            # Creating controled combinations

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

print 'Processing Single Core'
print os.getcwd()
print 'Password string: ', chars
print 'Password Lenghts: ', str(PW_LOW), ' - ', str(PW_HIGH)

# Mark the start time
startTime = time.time()

# Open a File for writing the results

try:
    # Open the output file
    fp = open('PW-ALL', 'w')
except:
    print 'File Processing Error'
    sys.exit(0)
    
# create a loop to include all passwords
# within the allowable range

pwCount = 0

for r in range(PW_LOW, PW_HIGH+1):
    
    #Apply the standard library interator
    for s in itertools.product(chars, repeat=r):
        
        # Hash each new password as they are
        # generated

        pw = ''.join(s)
        try:
            md5Hash = hashlib.md5()
            md5Hash.update(SALT+pw)
            md5Digest = md5Hash.hexdigest()
            
            # Write the hash, password pair to the file
            fp.write(md5Digest + ' ' + pw + '\n')
            pwCount += 1
            del md5Hash
        except:
            print 'File Processing Error'     
    
# Close the output file when complete
fp.close()    

# When complete calculate the elapsed time
elapsedTime = time.time() - startTime   
print 'Single Core Rainbow Complete'
print 'Elapsed Time: ', elapsedTime
print 'Passwords Generated: ', pwCount
print

