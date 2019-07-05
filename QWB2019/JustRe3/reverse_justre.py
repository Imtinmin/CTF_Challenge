flag=''

a='2A96B57D7ABF92ECFF0C1100B713614059FECC87D6F33CFE5B0F18F0577752405D6FD13F1E0F5F095053ED2B11BE185A5E875240623118B21FF3500954501B6625974D24229C8D2473101100FE0E61095A53EDFB826718006B35518BE8F358FE'.decode('hex')
b='558BEC83E4F081EC78020000A10450400033C4898424740200000F1005A8414000A0C0414000560F1144242C57F30F7E05B8414000660FD64424400F10410A6A408844244C8D8424FC0100006A00500F1144241CE8580F00006A408D84244802'.decode('hex')

for i in range(0x100):
    ta=int(a[:4][::-1].encode('hex'),16)
    tb=int(b[:4][::-1].encode('hex'),16)
    ta+=0x1010101*i
    ta&=0xffffffff
    tc=int(a[4:8][::-1].encode('hex'),16)
    td=int(b[4:8][::-1].encode('hex'),16)
    tc+=0x1010101*i
    tc&=0xffffffff
    if (td^tc)-(tb^ta) == 1:
        print hex(tb^ta),hex(i)
        flag+=hex(tb^ta)[2:-1]+hex(i)[2:]

from Crypto.Cipher import DES3

BS = DES3.block_size

def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):
    return s[0:-ord(s[-1])]

key='AFSAFCEDYCXCXACNDFKDCQXC'
mode=DES3.MODE_ECB
cipher=DES3.new(key, mode)

xa='FACE0987E6A97C50'.decode('hex')
xb='6C97BB90CF0DD520'.decode('hex')

print cipher.decrypt(xa[::-1]),cipher.decrypt(xb[::-1])
flag+=cipher.decrypt(xa[::-1])+cipher.decrypt(xb[::-1])

print flag
# flag{13242268130dcc509a6f75849b}