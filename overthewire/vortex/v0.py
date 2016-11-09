from pwn import * 
import struct

s = remote('vortex.labs.overthewire.org', 5842)

ints = []
for i in range(0,4):
    ints.append(struct.unpack("I", s.recv(4))[0])
log.info(ints)
s.send(str(p32(sum(ints))))
log.success(s.recv())
