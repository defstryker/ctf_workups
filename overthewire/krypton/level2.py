from pwn import *
shell = ssh('krypton2', 'krypton.labs.overthewire.org',
        password='ROTTEN')
sh = shell.run('bash')
sh.recvuntil("$ ")

sh.sendline(b'echo AAAAA > hola; chmod 755 .')
log.info(sh.recvuntil("$ ").decode())
sh.sendline(b'/krypton/krypton2/encrypt hola')
log.info(sh.recvuntil("$ ").decode())

# pass
