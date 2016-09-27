from pwn import *
shell = ssh('leviathan4', 'leviathan.labs.overthewire.org',
        password='vuH0coox6m')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################

sh.sendline('.trash/bin')
log.info(sh.recv(timeout=5).decode())
log.info(sh.recv(timeout=5).decode())


#pass Tith4cokei
