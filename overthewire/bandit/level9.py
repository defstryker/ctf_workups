from pwn import *
shell = ssh('bandit9', 'bandit.labs.overthewire.org',
    password='UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('strings data.txt | grep ==')
log.success(sh.recv(timeout=5).decode())

#pass truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
