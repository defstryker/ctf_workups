from pwn import *
import string
shell = ssh('bandit15', 'bandit.labs.overthewire.org',
    password='BfMYroe26WYalil77FoDi9qh59eK5xNr')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('echo BfMYroe26WYalil77FoDi9qh59eK5xNr | openssl s_client -connect localhost:30001 -quiet')

files = sh.recv(timeout=30).decode()
log.info(files)
log.info(sh.recv(timeout=30).decode())
log.info(sh.recv(timeout=30).decode())
log.info(sh.recv(timeout=30).decode())


#pass cluFn7wTiGryunymYOu4RcffSxQluehd
