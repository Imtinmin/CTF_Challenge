import base64
from pyDes import *
from random import choice
import string

def GenPassword(length=8,chars=string.ascii_letters):
    return ''.join([choice(chars) for i in range(length)])
 

def DesEncrypt(str):
    k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return EncryptStr.encode('hex')

def DesDecrypt(str):
	k = des(Des_Key, ECB, pad=None, padmode=PAD_PKCS5)
	DecryptStr = k.decrypt(str)
	return DecryptStr.encode('hex')
Des_Key = GenPassword().upper()

f1 = open('123.txt','wb')
f2 = open('enc.txt','rb')
content = f2.readlines()
for i in content:
	
	f1.write(DesDecrypt(i[:-1])+'\n')
f1.close()
f2.close()


