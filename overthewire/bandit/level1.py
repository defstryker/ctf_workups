from pwn import *
shell = ssh('bandit1', 'bandit.labs.overthewire.org',
    password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cat ./-')
log.success(sh.recv().decode())

#pass CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
