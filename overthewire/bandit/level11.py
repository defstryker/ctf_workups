from pwn import *
import string
shell = ssh('bandit11', 'bandit.labs.overthewire.org',
    password='IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

sh.sendline('cat data.txt')
b = sh.recv(timeout=5).decode()
log.info(b)

# caesar shift solved
# from the internet ...
ans = '5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'
log.success(ans)

#pass 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
