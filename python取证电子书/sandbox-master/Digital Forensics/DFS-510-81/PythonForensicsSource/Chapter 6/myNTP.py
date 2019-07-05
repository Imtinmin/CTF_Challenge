"""
Query an NTP server.

Author: T. Palmer
Initial Release: January 2018  Version 1.0.0
"""

import ntplib
import time

NIST = ['nist1-macon.macon.ga.us', 'time.apple.com', 'time.windows.com']

ntp = ntplib.NTPClient()

# Display the list of servers, and make things more human readable by adding
# one to the index
for index, server in enumerate(NIST):
    print str(index + 1) + ") " + server + "\n"

# Only allow integers between 1 and 3 to be entered
selectedIndex = 0
while 1 > selectedIndex or 3 < selectedIndex:
    try:
        selectedIndex = int(raw_input("Please enter server number (1 - 3): "))
    except ValueError:
        print "Please enter a number between 1 and 3"

# Assign the selected server to ntpServer, we're subtracting one from the
# entered value because list indexes start at 0
ntpServer = NIST[selectedIndex - 1]

# Gracefully query selected NTP server
ntpResponse = None
try:
    ntpResponse = ntp.request(ntpServer)
except Exception as e:
    print str(e) + "\n"

# If a response is received, continue on to displaying results
if ntpResponse:

    # Calculate the difference between the current system time and the time
    # taken to query the server
    now = time.time()
    diff = now - ntpResponse.tx_time

    print 'Response from ' + ntpServer + ': '
    print 'Difference: ' + str(diff) + ' seconds'
    print 'Network Delay: ' + str(ntpResponse.delay)

    # Use strftime to display timestamps in a friendly format
    nistTime = time.strftime(
        "%a, %d %b %Y %H:%M:%S +0000",
        time.gmtime(int(ntpResponse.tx_time))
    )
    systemTime = time.strftime(
        "%a, %d %b %Y %H:%M:%S +0000",
        time.gmtime(int(now))
    )
    print 'UTC NIST: ' + nistTime
    print 'UTC SYSTEM: ' + systemTime + "\n"
