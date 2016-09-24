from pwn import *
#context.log_level = 'debug'
shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cat readme')
log.success(sh.recv().decode())

#pass boJ9jbbUNNfktd78OOpsqOltutMc3MY1
