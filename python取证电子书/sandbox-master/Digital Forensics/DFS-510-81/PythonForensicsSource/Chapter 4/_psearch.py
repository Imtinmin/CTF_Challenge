#
# psearch support functions, where all the real work gets done
# 
# Display Message()                    ParseCommandLine()                                
# ValidateFileRead()                    ValidateFileWrite()
# Matrix (class)
#
# REVISION HISTORY
#
# 1/25/2015 
# Added support for the matching of phrases 
# Fixed small bug in hex printout code
#
# by: Chet Hosmer
# Modifications Identified by # CDH 1-25-2105
# 

import argparse         # Python Standard Library - Parser for command-line options, arguments
import os               # Standard Library OS functions
import logging          # Standard Library Logging functions
import sys              # Standard Library system related functions

log = logging.getLogger('main._psearch')

# Psuedo Constants 

# CDH 1-25-2015 Added MAX_PHRASE, Changed PREDECESSOR_SIZE 
#               AND WINDOW_SIZE to support phrases
#               Added a constant for the characeter ' ' or SPACE 

MIN_WORD = 5            # Minimum word size in bytes
MAX_WORD = 15           # Maximum word size in bytes
MAX_PHRASE = 80         # Maximum phrase size in bytes

PREDECESSOR_SIZE = 80   # Values to print before match found
WINDOW_SIZE = 240       # Total values to dump when match found

SPACE = ' '             # Added a constant for the space character


# Name: ParseCommand() Function
#
# Desc: Process and Validate the command line arguments
#           use Python Standard Library module argparse
#
# Input: none
#  
# Actions: 
#              Uses the standard library argparse to process the command line
#
def ParseCommandLine():

    parser = argparse.ArgumentParser('Python Search')

    parser.add_argument('-v', '--verbose',    help="enables printing of additional program messages", action='store_true')
    parser.add_argument('-k', '--keyWords',   type= ValidateFileRead, required=True, help="specify the file containing search words")
    # CDH 1-25-2015 Added Key Phrase Input File
    parser.add_argument('-p', '--keyPhrases', type= ValidateFileRead, required=True, help="specify the file containing search phrases") 
    parser.add_argument('-t', '--srchTarget', type= ValidateFileRead, required=True, help="specify the target file to search")    
    parser.add_argument('-m', '--theMatrix',  type= ValidateFileRead, required=True, help="specify the weighted matrix file")     
    
    global gl_args
    
    gl_args = parser.parse_args()           
    
    DisplayMessage("Command line processed: Successfully")

    return

# End Parse Command Line


#
# Name: ValidateFileRead Function
#
# Desc: Function that will validate that a file exists and is readable
#
# Input: A file name with full path
#  
# Actions: 
#              if valid will return path
#
#              if invalid it will raise an ArgumentTypeError within argparse
#              which will inturn be reported by argparse to the user
#

def ValidateFileRead(theFile):

    # Validate the path is a valid
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')

    # Validate the path is readable
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')

#End ValidateFileRead ===================================

#
# Name: DisplayMessage() Function
#
# Desc: Displays the message if the verbose command line option is present
#
# Input: message type string
#  
# Actions: 
#              Uses the standard library print function to display the messsage
#
def  DisplayMessage(msg):

    if gl_args.verbose:
        print(msg)

    return   

#End DisplayMessage=====================================

# 
# Name SearchWords()
#
# Uses command line arguments
#
# Searches the target file for keywords
#

def SearchWords():
    
    # Create an empty set of search words
    
    searchWords   = set()
    
    # CDH 1-25-2015 Added set to hold phrases to search for
    searchPhrases = set()

    # Attempt to open and read search words
    try:
        fileWords = open(gl_args.keyWords)
        for line in fileWords:
            searchWords.add(line.strip())    
    except:
        log.error('Keyword File Failure: ' + gl_args.keyWords)
        sys.exit()   
    finally:
        fileWords.close()
        
    # CDH 1-25-2015
    # Attempt to open and read KeyPhrases
    # and store them in the set searchPhrases
    # ++++++++++++++++++++++++++++++++++++++++++++
    try:
        filePhrase = open(gl_args.keyPhrases)
        for line in filePhrase:
            searchPhrases.add(line.strip())    
    except:
        log.error('Phrase File Failure: ' + gl_args.keyPhrases)
        sys.exit()   
    finally:
        filePhrase.close()        
    # +++++++++++++++++++++++++++++++++++++++++++
    
    # Create Log Entry Words to Search For
    
    log.info('Search Words')
    log.info('Input File: '+gl_args.keyWords)
    log.info(searchWords)

    # Create Log Entry Words to Search For
    
    log.info('Search Phrases')
    log.info('Input File: '+gl_args.keyPhrases)
    log.info(searchPhrases)
    
    # Attempt to open and read the target file
    # and directly load into a bytearray
    
    try:
        targetFile = open(gl_args.srchTarget, 'rb')
        baTarget = bytearray(targetFile.read())
    except:
        log.error('Target File Failure: ' + gl_args.srchTarget)
        sys.exit()
    finally:
        targetFile.close()

    sizeOfTarget= len(baTarget)

    # Post to log
    
    log.info('Target of Search: ' + gl_args.srchTarget)
    log.info('File Size: '+str(sizeOfTarget))

    baTargetCopy = baTarget

    wordCheck = class_Matrix()
    
    # Search Loop
    # step one, replace all non characters with zero's

    # CDH 01-25-2014 Allow Alpha Characters
    # A-Z, a-z and spaces only 
    # Everything else is converted to zero
    
    for i in range(0, sizeOfTarget):
        character = chr(baTarget[i])
        if not character.isalpha() and character != SPACE:
            baTarget[i] = 0
                    
    # step # 2 extract possible words from the bytearray
    # and then inspect the search word list
    # create an empty list of probable wnot found items
    
    indexOfWords = []

    cnt = 0
    for i in range(0, sizeOfTarget):
        character = chr(baTarget[i])
        # CDH 1-25-2015
        # Allow alpha and spaces during collection
        if character.isalpha() or character == SPACE:
            cnt += 1
        else:
            # CDH 1-25-2015
            #     Modified Check for MAX PHRASE
            if (cnt >= MIN_WORD and cnt <= MAX_PHRASE):
                
                #+++++++++++++++++++++++++++++++++++++++++++++++++++
                # CDH 1-25-2015 collect possible phrase
                #               a phrase = words separated by spaces
                #               the following section is added
                #+++++++++++++++++++++++++++++++++++++++++++++++++++
                newPhrase = ""
                for z in range(i-cnt, i):
                    newPhrase = newPhrase + chr(baTarget[z])
                
                newPhrase = newPhrase.lower()
                
                # Search all phrases for a potential match
                
                for eachPhrase in searchPhrases:
                    # Determine if newPhrase is contained in eachPhrase
                    # if newPhrase.count(eachPhrase) > 0:
                    if eachPhrase in newPhrase:
                        # If the phrase matches one of the phrases
                        # then Print the Buffer
                        PrintBuffer(newPhrase, i-cnt, baTargetCopy, i-PREDECESSOR_SIZE, WINDOW_SIZE) 
                        cnt = 0
                        print
                
                # CDH 1-25-2015 End Collect Possible Phrases Section 
                #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # CDH 1-25-2015 Now that we have a phrase
                #               we can split the phrase into possible words
                #               new section starts here
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                # Create a list of words found in the phrase
                # Using the the .split() method of the data type strings
                
                splitWordList = newPhrase.split()
                
                # Loop through the possible words in the splitWordList
                
                for eachWord in splitWordList:
                    
                    # Check the word against the word list
                    # CDH 1-25-2015 This section did not change from orginal
                    #               Except that it is inside the for loop
                    #               in order to process each word in the 
                    #               splitWordList
                    
                    if (eachWord in searchWords):
                        PrintBuffer(eachWord, i-cnt, baTargetCopy, i-PREDECESSOR_SIZE, WINDOW_SIZE) 
                        indexOfWords.append([eachWord, i-cnt])
                        cnt = 0
                        print
                    else:
                        if wordCheck.isWordProbable(eachWord):
                            indexOfWords.append([eachWord, i-cnt])
                        cnt = 0    
            else:        
                cnt = 0
                
    PrintAllWordsFound(indexOfWords)

    return

# End of SearchWords Function
    
#
# Print Hexidecimal / ASCII Page Heading
#

def PrintHeading():

    print("Offset        00  01  02  03  04  05  06  07  08  09  0A  0B  0C  0D  0E  0F         ASCII")
    print("------------------------------------------------------------------------------------------------")
    
    return
# End PrintHeading

#
# Print Buffer
#
# Prints Buffer contents for words that are discovered
# parameters
# 1) Word found
# 2) Direct Offset to beginning of the word
# 3 buff The bytearray holding the target
# 4) offset starting position in the buffer for printing
# 5) hexSize, size of hex display windows to print
#
def PrintBuffer(word, directOffset, buff, offset, hexSize):
    
    print "Found: "+ word + " At Address: ",
    print "%08x     " % (directOffset)    
    
    PrintHeading()
    
    for i in range(offset, offset+hexSize, 16):
        for j in range(0,17):
            if (j == 0):
                print "%08x     " % i,
            else:
                byteValue = buff[i+j]
                print "%02x " % byteValue,
        print "      ",
        
        # CDH 1-25-2015 Fixed Small Bug in Print Buffer
        # Changed 2nd value in range parameter to 16 vs 17
        
        for j in range (0,16):
            byteValue = buff[i+j]
            if (byteValue >= 0x20 and byteValue <= 0x7f):
                print "%c" % byteValue,
            else:
                print '.',
        print
    
    return

# End Print Buffer

#
# PrintAllWordsFound
#

def PrintAllWordsFound(wordList):
    
    print "Index of All Words"
    print "---------------------"
   
    wordList.sort()
    
    for entry in wordList:
        print entry

    print "---------------------"
    print
    
    return

    
#End PrintAllWordsFound
                          
# 
# Class Matrix
#
# init method, loads the matrix into the set
# weightedMatrix
#
# isWordProbable method
#   1) Calcuates the weight of the provided word
#   2) Verifies the minimum length
#   3) Calculates the weight for the word
#   4) Tests the word for exsistance in the matrix
#   5) Returns true or fales
#

class class_Matrix:
    
    weightedMatrix = set()
    
    def __init__(self):
        try:
                fileTheMatrix = open(gl_args.theMatrix, 'rb')
                for line in fileTheMatrix:
                        value = line.strip()
                        if len(value) > 2:
                            self.weightedMatrix.add(int(value,16))       
        except:
            log.error('Matrix File Error: ' + gl_args.theMatrix)
            DisplayMessage("Matrix File Load Error")
            sys.exit()   
        finally:
            fileTheMatrix.close()        

        return
    
    def isWordProbable(self, theWord):
        
        if (len(theWord) < MIN_WORD):
            return False
        else:
            BASE = 96
            wordWeight = 0
            
            for i in range(4,0,-1):
                charValue = (ord(theWord[i]) - BASE)
                shiftValue = (i-1)*8
                charWeight = charValue << shiftValue
                wordWeight = (wordWeight | charWeight)        
                
            if ( wordWeight in self.weightedMatrix):
                    return True
            else:
                    return False
                    
## End Class Matrix

