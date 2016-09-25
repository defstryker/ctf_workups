from pwn import *
shell = ssh('leviathan0', 'leviathan.labs.overthewire.org',
        password='leviathan0')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
sh.sendline('cat .backup/bookmarks.html | grep password')
ret = sh.recv(timeout=10).decode()
log.info(ret)

# after reading through that...
log.success('rioGegei8m')

#pass rioGegei8m
