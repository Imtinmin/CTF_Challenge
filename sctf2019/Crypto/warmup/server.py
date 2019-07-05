#!/usr/bin/python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from Crypto.Random import get_random_bytes
from FLAG import flag

class MAC:
    def __init__(self):
        self.key = get_random_bytes(16)
        self.iv = get_random_bytes(16)

    def pad(self, msg):
        pad_length = 16 - len(msg) % 16
        return msg + chr(pad_length) * pad_length

    def unpad(self, msg):
        return msg[:-ord(msg[-1])]

    def code(self, msg):
        res = chr(0)*16
        for i in range(len(msg)/16):
            res = strxor(msg[i*16:(i+1)*16], res)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        return aes.encrypt(res).encode('hex')

    def identity(self, msg, code):
        if self.code(msg) == code:
            msg = self.unpad(msg)
            if msg == 'please send me your flag':
                print 'remote: ok, here is your flag:%s' % flag
            else:
                print 'remote: I got it'
        else:
            print 'remote: hacker!'


if __name__ == '__main__':
    mac = MAC()
    message = 'see you at three o\'clock tomorrow'
    print 'you seem to have intercepted something:{%s:%s}' %(mac.pad(message).encode('hex'), mac.code(mac.pad(message)))
    print 'so send your message:'
    msg = raw_input()
    print 'and your code:'
    code = raw_input()
    mac.identity(msg.decode('hex'), code)
    exit()

