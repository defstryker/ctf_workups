from pwn import *
import string
shell = ssh('bandit13', 'bandit.labs.overthewire.org',
    password='8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('ls -la')
files = sh.recv(timeout=10).decode()
log.info(files)

shell.download_file('sshkey.private')

#pass **No password. Instead get a ssh-key**
