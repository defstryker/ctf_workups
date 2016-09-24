from pwn import *
import string
shell = ssh('bandit12', 'bandit.labs.overthewire.org',
    password='5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls')
files = sh.recv().decode()
log.info(files)

shell.download_file('data.txt')

# have to go through a sequence of decompressing
# downloaded the file and worked on it offline

#pass 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
