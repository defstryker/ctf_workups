from pwn import *
shell = ssh('bandit3', 'bandit.labs.overthewire.org',
    password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cat inhere/.hidden')
log.success(sh.recv().decode())

#pass pIwrPrtPN36QITSp3EQaw936yaFoFgAB
