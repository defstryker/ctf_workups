from pwn import *
shell = ssh('bandit5', 'bandit.labs.overthewire.org',
    password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cd inhere')
log.info(sh.recv().decode())
#sh.recv().decode(timeout=3)

sh.sendline('find ./ ! -executable -size 1033c 2>/dev/null')
sh.recv(timeout=3).decode()
ans = sh.recv(timeout=3).decode()
log.info(ans)

sh.sendline('cat {}'.format(ans))
log.success(sh.recv(timeout=3).decode())
log.success(sh.recv(timeout=3).decode())

#pass DXjZPULLxYr17uwoI01bNLQbtFemEgo7
