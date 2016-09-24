from pwn import *
shell = ssh('bandit6', 'bandit.labs.overthewire.org',
    password='DXjZPULLxYr17uwoI01bNLQbtFemEgo7')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('find / -size 33c -user bandit7 -group bandit6 2>/dev/null')
ans = sh.recv(timeout=5).decode()
log.info(ans)

sh.sendline('cat {}'.format(ans))
log.info(sh.recv(timeout=5).decode())
log.success(sh.recv(timeout=5).decode())

#pass HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
