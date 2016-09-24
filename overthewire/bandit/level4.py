from pwn import *
shell = ssh('bandit4', 'bandit.labs.overthewire.org',
    password='pIwrPrtPN36QITSp3EQaw936yaFoFgAB')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cd inhere')
log.info(sh.recv().decode())
sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cat ./-file07')
log.success(sh.recv().decode())

#pass koReBOKuIDDepwhWk7jZC0RTdopnAYKh
