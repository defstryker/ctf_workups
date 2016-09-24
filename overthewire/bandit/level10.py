from pwn import *
import base64
shell = ssh('bandit10', 'bandit.labs.overthewire.org',
    password='truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cat data.txt')
b = sh.recv(timeout=5).decode()
log.success(base64.b64decode(b).decode())

#pass IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
