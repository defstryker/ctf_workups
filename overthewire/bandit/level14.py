from pwn import *
import string
shell = ssh('bandit14', 'bandit.labs.overthewire.org',
    keyfile='sshkey.private')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cat /etc/bandit_pass/bandit14 | nc localhost 30000')
files = sh.recv(timeout=10).decode()
log.info(files)

#pass BfMYroe26WYalil77FoDi9qh59eK5xNr
