from pwn import *
context(arch='i386', os='linux')

shell = ssh('behemoth0', 'behemoth.labs.overthewire.org', 22, 'behemoth0')
sh = shell.run('/behemoth/behemoth0')
sh.sendline('eatmyshorts')
log.info(sh.recvuntil('$ '))
sh.sendline('cat /etc/behemoth_pass/behemoth1')
log.success(sh.recvuntil('$'))

