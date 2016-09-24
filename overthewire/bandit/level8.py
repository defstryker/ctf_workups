from pwn import *
shell = ssh('bandit8', 'bandit.labs.overthewire.org',
    password='cvX2JJa4CFALtqS87jk27qwqGhBM9plV')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cat data.txt | sort | uniq -u')
log.success(sh.recv(timeout=5).decode())

#pass UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
