from pwn import *
shell = ssh('fd', 'pwnable.kr', password='guest', port=2222)
sh = shell.run('bash')
sh.recv().decode()
context.log_level = 'debug'
