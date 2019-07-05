import ntplib
import time

NIST = 'nist1-macon.macon.ga.us'

ntp = ntplib.NTPClient()

ntpResponse = ntp.request(NIST)

if (ntpResponse):
    now = time.time()
    diff = now-ntpResponse.tx_time
    print 'Difference        : ',
    print diff,
    print 'seconds'

    print 'Network Delay : ',
    print ntpResponse.delay

    print 'UTC NIST          :  ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(ntpResponse.tx_time)))
    print 'UTC SYSTEM    :  ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(now)))

else:
    print 'No Response from Time Service'
    