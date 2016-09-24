from pwn import *
shell = ssh('bandit7', 'bandit.labs.overthewire.org',
    password='HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cat data.txt | grep millionth')
log.success(sh.recv(timeout=5).decode())

#pass cvX2JJa4CFALtqS87jk27qwqGhBM9plV
