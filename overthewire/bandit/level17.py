from pwn import *
import string
shell = ssh('bandit17', 'bandit.labs.overthewire.org',
    keyfile='level17key')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('diff passwords.new passwords.old')
log.info(sh.recv(timeout=5).decode())
sh.sendline('cat /etc/bandit_pass/bandit17')
log.info(sh.recv(timeout=5).decode())

#pass kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
