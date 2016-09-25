from pwn import *
shell = ssh('leviathan1', 'leviathan.labs.overthewire.org',
        password='rioGegei8m')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################
# downloading the 'check' file to locally
# attempt to crack it
#shell.download_file('check')

sh.sendline('./check')
sh.sendline('sexsecret?godlove?')
log.info(sh.recv(timeout=10).decode())
log.info(sh.recv(timeout=3).decode())
sh.sendline('cat /etc/leviathan_pass/leviathan2')
log.success(sh.recv(timeout=10).decode())

#pass
