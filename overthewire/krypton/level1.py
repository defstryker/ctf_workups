from pwn import *
pw = b64d('S1JZUFRPTklTR1JFQVQ=').decode()
log.success(pw)
shell = ssh('krypton1', 'krypton.labs.overthewire.org',
        password=pw)
sh = shell.run('bash')
sh.recvuntil("$ ")
sh.sendline(b'cat /krypton/krypton1/krypton2')
log.info(sh.recvuntil("$ ").decode())

# pass LEVEL TWO PASSWORD ROTTEN
