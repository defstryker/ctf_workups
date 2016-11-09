### !!!! does not work. but completed through direct ssh

# default section for most solutions.
from pwn import *
shell = ssh('col', 'pwnable.kr', password='guest', port=2222)
sh = shell.run('bash')
sh.recv().decode()
#####################################
#b = struct.pack("<L", int('0x21DD09EC',16) // 5) * 4 + \
#struct.pack("<L",int('0x06c5cecc', 16))

sh.sendline('./col $(perl -e \'print \"\xc8\xce\xc5\x06\"x4 . \"\xcc\xce\xc5\x06\"\')')
log.info(sh.recv().decode())
