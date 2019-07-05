import argparse                        # Python Standard Library - Parser for command-line options, arguments
import os                                  # Standard Library OS functions

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

    parser = argparse.ArgumentParser('Python gpsExtractor')

    parser.add_argument('-v', '--verbose',    help="enables printing of additional program messages", action='store_true')
    parser.add_argument('-l', '--logPath',       type= ValidateDirectory, required=True, help="specify the directory for forensic log output file")       
    parser.add_argument('-c ', '--csvPath',     type= ValidateDirectory, required=True, help="specify the output directory for the csv file")    
    parser.add_argument('-d', '--scanPath',  type= ValidateDirectory, required=True, help="specify the directory to scan")
      
    theArgs = parser.parse_args()           

    return theArgs

# End Parse Command Line ===========================

def ValidateDirectory(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # Validate the path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')

#End ValidateDirectory ===================================