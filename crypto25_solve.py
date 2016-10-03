#!/usr/bin/env python

import subprocess

def cmd(c):
    process = subprocess.Popen(c.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))
    return res


def main():
    cipher = cmd("./crypto25.py").strip().decode('hex')

    payload = "\x41" * len(cipher)    
    
    c = "./crypto25.py {} {}".format(0, payload)

    res = cmd(c).strip().decode('hex')
    keystream = xor(payload, res)

    print "Decoding..."
    print xor(cipher, keystream)
    
if __name__ == "__main__":
    main()
