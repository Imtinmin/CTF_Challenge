#! /usr/bin/env python
# -*- coding: utf-8 -*-
from secret import FLAG
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, isPrime, getRandomNBitInteger
from libnum import invmod
import gmpy2

def destroy(x, num):
	while True:
		dt = getRandomNBitInteger(num)
		r = x ^ dt
		if isPrime(r):
			return r

flag = bytes_to_long(FLAG)

p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = getRandomNBitInteger(50)
phi_n = (p-1)*(q-1)
while gmpy2.gcd(e, phi_n) != 1:
    e = getRandomNBitInteger(50)
d = invmod(e, phi_n)

with open("info","a") as f:
	f.write("n: "+hex(n)+'\n')
	f.write("e*d: " + hex(e*d) + '\n\n')

print "Destroy p, q"
new_p = destroy(p, 800)
new_q = destroy(q, 800)
new_n = new_p * new_q
new_phin = (new_p-1)*(new_q-1)
e1 = getRandomNBitInteger(50)
while gmpy2.gcd(e1, new_phin) != 1:
    e1 = getRandomNBitInteger(50)
d1 = invmod(e1, new_phin)

with open("info","a") as f:
    f.write("Destroy p, q\n")
    f.write("new n: "+hex(new_n)+'\n')
    f.write("dp: "+ hex(d1 % (new_p - 1))+'\n')
    f.write("dq: "+hex(d1 % (new_q - 1)))

c = pow(flag, e1, new_n)

with open("cipher","w") as f:
    f.write("enc_flag: "+hex(c))

