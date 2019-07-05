import base64
import binascii
import collections
import hashlib
import os
import random
import string
import libnum
from Crypto.Util import number
from Crypto.Util.strxor import strxor
flag1 = int('flag1{*******************}'.encode('hex'),16)
flag2 = int('flag2{*******************}'.encode('hex'),16)
flag = int('flag{*******************}'.encode('hex'),16)
flag = flag1*flag2*flag
flag = libnum.n2s(flag)
p = number.getPrime(1024)
q = number.getPrime(1024)
n = p * q
e = number.getPrime(24)

def final(data):
    iv = os.urandom(256)
    fff = iv
    lll = binascii.hexlify(data)
    ooo = (len(lll) + 3) // 4
    kkk = lll.ljust(ooo * 4, b'f')
    for i in range(0, len(kkk), 4):
        qqq = number.bytes_to_long(kkk[i:i+4])
        www = pow(qqq, e, n)
        eee = binascii.unhexlify('%.512x' % www)
        fff += strxor(fff[-256:], eee)
    return base64.b64encode(fff)
f = open('enc','wb')
f.write('n=0x%x, e=0x%x' % (n, e))
f.write('\n')
f.write(final(flag))
f.close()