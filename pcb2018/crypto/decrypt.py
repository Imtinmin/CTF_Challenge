#!usr/bin/python 
#_*_ coding=UTF-8 _*_

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Crypto import Random
import sys


class aesdemo:
    #aes = AES.new(key,mode)
    def __init__(self,key):
        self.key = key
        #self.BS=BS


    def pad(self,msg):
        #BS = AES.block_size 
        # aes数据分组长度为128 bit
        byte = 16 - len(msg) % 16
        return msg + chr(byte) * byte
    def unpad(self,msg):
        if not msg:
            return ''
        return msg[:-ord(msg[-1])]      

    def xor(self,a, b):
            #assert len(a) == len(b)
            return ''.join([chr(ord(ai)^ord(bi)) for ai, bi in zip(a,b)])

    def split_by(self,data,step):
            return [data[i : i+step] for i in xrange(0, len(data), step)]

    def encrypt(self, plaintext):
        # 生成随机初始向量IV
        iv = Random.new().read(16)
        aes = AES.new(self.key,AES.MODE_CBC,iv)
        prev_pt = iv
        prev_ct = iv
        ct=""

        msg=self.pad(plaintext)
        for block in self.split_by(msg, 16):
            ct_block = self.xor(block, prev_pt)
            ct_block = aes.encrypt(ct_block)
            ct_block = self.xor(ct_block, prev_ct)
            ct += ct_block

        return b2a_hex(iv + ct)

    def decrypt(self,cipher):
        c=a2b_hex(cipher)
        iv=c[:16]
        cipher=c[16:]
        aes = AES.new(self.key,AES.MODE_CBC,iv)
        prev_pt = iv
        prev_ct = iv
        pl=""

        msg=cipher
        for block in self.split_by(msg, 16):
            p_block = self.xor(block, prev_pt)
            p_block = aes.decrypt(p_block)
            p_block = self.xor(p_block, prev_ct)
            pl += p_block
        return self.unpad(pl)
# 测试模块
if __name__ == '__main__':
    cipher="524160f3d098ad937e252494f827f8cf26cc549e432ff4b11ccbe2d8bfa76e5c6606aad5ba17488f11189d41bca45baa"
    BS = AES.block_size # aes数据分组长度为128 bit
    key="asdfghjkl1234567890qwertyuiopzxc"
    demo = aesdemo(key)
    e = demo.encrypt("a"*16)
    p = demo.decrypt(cipher)
    print p