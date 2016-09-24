from pwn import *
shell = ssh('bandit2', 'bandit.labs.overthewire.org',
    password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9')
sh = shell.run('bash')
sh.recv().decode()

sh.sendline('cat "spaces in this filename"')
log.success(sh.recv().decode())

#pass UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
