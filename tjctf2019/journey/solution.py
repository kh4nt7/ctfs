#!/usr/bin/python

from pwn import *

# Connection
p = remote('p1.tjctf.org', 8009)
attempts = 0
while True:
    word = p.recvline()
    
    # Check if flag in first recv
    if "tjctf" in word: 
        print word
        break

    # Find encountered word
    word = ''.join(re.findall(r"'(.*?)'", word))
    print "[*]Encountered:", word
    step = p.recvuntil('step:')
    
    # Check if flag in second recv
    if "tjctf" in step: 
        print step
        break

    # Journey Continued
    print "[*]Sending:", word
    p.sendline(word)
    attempts += 1
    print "[+] Attemps: %d" % attempts
    print
