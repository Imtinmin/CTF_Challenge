# Packet Extractor / Decoder Module
# 

import socket, sys
from struct import *

# Constants
PROTOCOL_TCP = 6
PROTOCOL_UDP = 17

# PacketExtractor
#
# Purpose: Extracts fields from the IP, TCP and UDP Header
#
# Input:   packet: buffer from socket.recvfrom() method
#          displaySwitch: True: Display the details, False omits
# Output:  result list containing
#                      protocol, srcIP, srcPort, dstIP, dstPort
#
def PacketExtractor(packet, displaySwitch):

    #Strip off the first 20 characters for the ip header
    stripPacket = packet[0:20]
     
    #now unpack them
    ipHeaderTuple = unpack('!BBHHHBBH4s4s' , stripPacket)
        
    # unpack returns a tuple, for illustration I will extract
    # each individual values
                                           # Field Contents
    verLen       = ipHeaderTuple[0]        # Field 0: Version and Length
    dscpECN      = ipHeaderTuple[1]        # Field 1: DSCP and ECN                                        
    packetLength = ipHeaderTuple[2]        # Field 2: Packet Length
    packetID     = ipHeaderTuple[3]        # Field 3: Identification  
    flagFrag     = ipHeaderTuple[4]        # Field 4: Flags and Fragment Offset
    timeToLive   = ipHeaderTuple[5]        # Field 5: Time to Live (TTL)
    protocol     = ipHeaderTuple[6]        # Field 6: Protocol Number 
    checkSum     = ipHeaderTuple[7]        # Field 7: Header Checksum
    sourceIP     = ipHeaderTuple[8]        # Field 8: Source IP
    destIP       = ipHeaderTuple[9]        # Field 9: Destination IP    
    
    # Calculate / Convert extracted values
    
    version      = verLen >> 4             # Upper Nibble is the version Number
    length       = verLen & 0x0F           # Lower Nibble represents the size
    ipHdrLength  = length * 4              # Calculate the header length in bytes
    
    # covert the source and destination address to typical dotted notation strings
       
    sourceAddress = socket.inet_ntoa(sourceIP);
    destinationAddress = socket.inet_ntoa(destIP);
    
    if displaySwitch:
        print 'IP HEADER'
        print '-----------------------'
        print 'Version:         ' + str(version)
        print 'Packet Length:   ' + str(packetLength) + ' bytes'
        print 'Header Length:   ' + str(ipHdrLength) + ' bytes'
        print 'TTL:             ' + str(timeToLive) 
        print 'Protocol:        ' + str(protocol) 
        print 'Checksum:        ' + hex(checkSum)
        print 'Source IP:       ' + str(sourceAddress)
        print 'Destination IP:  ' + str(destinationAddress)
     
    # ------------------
    
    if protocol == PROTOCOL_TCP:
        
        stripTCPHeader = packet[ipHdrLength:ipHdrLength+20]
             
        # unpack returns a tuple, for illustration I will extract
        # each individual values using the unpack() function

        tcpHeaderBuffer = unpack('!HHLLBBHHH' , stripTCPHeader)
         
        sourcePort             = tcpHeaderBuffer[0]
        destinationPort        = tcpHeaderBuffer[1]
        sequenceNumber         = tcpHeaderBuffer[2]
        acknowledgement        = tcpHeaderBuffer[3]
        dataOffsetandReserve   = tcpHeaderBuffer[4]
        tcpHeaderLength        = (dataOffsetandReserve >> 4) * 4
        tcpChecksum            = tcpHeaderBuffer[7]
         
        if displaySwitch:
            print
            print 'TCP Header'
            print '-------------------'
            
            print 'Source Port:       ' + str(sourcePort)
            print 'Destination Port : ' + str(destinationPort) 
            print 'Sequence Number :  ' + str(sequenceNumber) 
            print 'Acknowledgement :  ' + str(acknowledgement)
            print 'TCP Header Length: ' + str(tcpHeaderLength) + ' bytes'
            print 'TCP Checksum:      ' + hex(tcpChecksum)
            print
            
        return(['TCP', sourceAddress, sourcePort, destinationAddress, destinationPort])
    
    elif protocol == PROTOCOL_UDP:
        
        stripUDPHeader = packet[ipHdrLength:ipHdrLength+8]
             
        # unpack returns a tuple, for illustration I will extract
        # each individual values using the unpack() function

        udpHeaderBuffer = unpack('!HHHH' , stripUDPHeader)
         
        sourcePort             = udpHeaderBuffer[0]
        destinationPort        = udpHeaderBuffer[1]
        udpLength              = udpHeaderBuffer[2]
        udpChecksum            = udpHeaderBuffer[3]
 
        if displaySwitch:
            
            print
            print 'UDP Header'
            print '-------------------'
            
            print 'Source Port:       ' + str(sourcePort)
            print 'Destination Port : ' + str(destinationPort) 
            print 'UDP Length:        ' + str(udpLength) + ' bytes'
            print 'UDP Checksum:      ' + hex(udpChecksum)
            print
        
        return(['UDP', sourceAddress, sourcePort, destinationAddress, destinationPort])
        
        
    else:
        
        # For expansion protocol support
        
        if displaySwitch:
            print 'Found Protocol : ' + str(protocol)
        
        return(['Unsupported',sourceAddress,0,destinationAddress,0])
        
    

