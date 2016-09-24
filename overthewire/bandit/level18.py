from pwn import *
import string
shell = ssh('bandit18', 'bandit.labs.overthewire.org',
    password='kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd')

log.critical(shell['/bin/cat readme'])
shell.download_file('readme')


#pass IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
