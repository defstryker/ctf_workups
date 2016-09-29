from pwn import *

# vars ...
user = 'narnia1'
host = 'narnia.labs.overthewire.org'
password = 'efeidiedae'
shell = ssh(user, host, password=password)
sh = shell.run('bash')
sh.recvuntil('$ ')
############################################
sh.sendline('cd /narnia/')
sh.recvuntil('$ ')
sh.sendline('./narnia1')
log.info(sh.recv(timeout=10).decode())


#pass
