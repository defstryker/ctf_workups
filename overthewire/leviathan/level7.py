from pwn import *
shell = ssh('leviathan7', 'leviathan.labs.overthewire.org',
        password='ahy7MaeBo9')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################

sh.sendline('cat CONGRATULATIONS')
log.success(sh.recv(timeout=10).decode())
log.success('Done with the lord. \m/')
