from pwn import *
shell = ssh('leviathan3', 'leviathan.labs.overthewire.org',
        password='Ahdiemoo1j')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################

sh.sendline('(echo \'snlprintf\'; cat) | ./level3')
log.info(sh.recv(timeout=30).decode())
sh.sendline('whoami')
log.info(sh.recv(timeout=30).decode())
sh.sendline('cat /etc/leviathan_pass/leviathan4')
log.success(sh.recv(timeout=30).decode())

#pass vuH0coox6m
