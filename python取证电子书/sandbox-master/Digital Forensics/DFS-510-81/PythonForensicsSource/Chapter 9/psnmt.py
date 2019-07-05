#
# Python Passive Network Monitor and Mapping Tool
#

# Import Standard Library Modules
import socket           # network interface library used for raw sockets
import signal           # generation of interrupt signals i.e. timeout
import os               # operating system functions i.e. file I/o
import sys              # system level functions i.e. exit()

# Import application specific Modules
import decoder          # module to decode tcp and udp packets
import _commandParser   # parse out command line args
import _csvHandler      # output generation
from   _classLogging import _ForensicLog  # Logging operations

# Process the Command Line Arguments
userArgs = _commandParser.ParseCommandLine()
  
# create a log object
logPath = os.path.join(userArgs.outPath,"ForensicLog.txt")
oLog = _ForensicLog(logPath)
  
oLog.writeLog("INFO", "PS-NMT Started")
  
csvPath = os.path.join(userArgs.outPath,"ps-nmtResults.csv")
oCSV = _csvHandler._CSVWriter(csvPath) 

# Setup the protocol to capture

if userArgs.TCP:
    PROTOCOL = socket.IPPROTO_TCP
elif userArgs.UDP:
    PROTOCOL = socket.IPPROTO_UDP
else:
    print 'Capture protocol not selected'
    sys.exit()

# Setup whether output should be verbose

if userArgs.verbose:
    VERBOSE = True
else:
    VERBOSE = False
    
# Calculate capture duration
captureDuration = userArgs.minutes * 60

# Create timeout class to handle capture duration

class myTimeout(Exception):
    pass

# Create a signal handler that raises a timeout event
# when the capture duration is reached

def handler(signum, frame):
    print 'timeout received', signum
    raise myTimeout()

# Enable Promiscious Mode on the NIC

ret =  os.system("ifconfig eth0 promisc")

if ret == 0:
    
    oLog.writeLog("INFO", 'Promiscious Mode Enabled')
    # create an INET, raw socket
    # AF_INET specifies       ipv4
    # SOCK_RAW specifies      a raw protocol at the network layer
    # IPPROTO_TCP or UDP      Specifies the protocol to capture   
    try:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, PROTOCOL)
        oLog.writeLog("INFO", 'Raw Socket Open')
    except:
        # if socket open fails
        oLog.writeLog("ERROR", 'Raw Socket Open Failed')
        del oLog
        if VERBOSE:
            print 'Error Opening Raw Socket'
        sys.exit()
    
    # Set the signal handler to the duraton specified by the user
    
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(captureDuration)
    
    # create a list to hold the results from the packet capture
    # I'm only interested in Protocol Source IP, Source Port, Destination IP, Destination Port
    
    ipObservations = []    
    
    # Begin receiving packets until duration is received
    # the inner while loop will execute until the timeout
    
    try:
    
        while True:
            
            # attempt recieve (this call will wait)
            recvBuffer, addr = mySocket.recvfrom(255)
            
            # decode the received packet
            content = decoder.PacketExtractor(recvBuffer, VERBOSE)

            # append the results to our list
            ipObservations.append(content)

            # write details to the forensic log file
            oLog.writeLog('INFO', \
                          '  RECV: ' + content[0] + \
                          '  SRC : ' + content[1] + \
                          '  DST : ' + content[3])
        
    except myTimeout:
        pass

    # Once time has expired disable Promiscous Mode
    ret =  os.system("ifconfig eth0 -promisc")
    oLog.writeLog("INFO", 'Promiscious Mode Diabled')
    
    # Close the Raw Socket
    mySocket.close()
    oLog.writeLog("INFO", 'Raw Socket Closed')
    
    # Create unique sorted list
    
    uniqueSrc = set(map(tuple, ipObservations))
    finalList = list(uniqueSrc)
    finalList.sort()
    
    # Write each unique sorted packet to the csv file
    for packet in finalList:
        oCSV.writeCSVRow(packet)
    
    oLog.writeLog('INFO', 'Program End')
    
    # Close the Log and CSV objects
    del oLog
    del oCSV
    
else:
    print 'Promiscious Mode not Set'
