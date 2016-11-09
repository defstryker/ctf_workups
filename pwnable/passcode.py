from pwn import *
shell = ssh('passcode', 'pwnable.kr', port=2222,
        password='guest')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())

sh.sendline('ls -la')
log.info(sh.recv(timeout=20).decode())
log.info(sh.recv(timeout=20).decode())

#shell.download_file('passcode.c')
shell.download_file('flag')
#\333\345\342
