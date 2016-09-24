from pwn import *
import string
shell = ssh('bandit16', 'bandit.labs.overthewire.org',
    password='cluFn7wTiGryunymYOu4RcffSxQluehd')
sh = shell.run('bash')
sh.recv().decode()

#sh.interactive()
# ^^ to find ports

sh.sendline('cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:31790 -quiet')
log.info(sh.recv(timeout=3).decode())
log.info(sh.recv(timeout=3).decode())
files = sh.recv(timeout=3).decode()
log.info(files)
log.info(sh.recv(timeout=3).decode())

#pass "ssh-key-file:level17key"
