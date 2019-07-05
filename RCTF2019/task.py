from Crypto.Util.number import *
from flag import FLAG
import gmpy2
Nbits = 512


K = [bytes_to_long(FLAG)]
for i in range(0xff):
    K = K + [getRandomInteger(Nbits)]

M = getPrime(Nbits)

def f(x, k, m):
    r = 0
    for i in range(len(k)):
        r = (r + k[i] * pow (x, i, m)) % m
    return x, r


for i in range(0x200):
    print "f(%d) = %d" % f(getRandomInteger(Nbits), K, M)
