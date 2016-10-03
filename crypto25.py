#!/usr/bin/env python

import sys
import struct
import base64
from Crypto.Cipher import AES


def pack(p):
    return struct.pack("<q", p)


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))

    return res


def keystream(key, length):
    keystr = ""
    aes = AES.new(key, AES.MODE_ECB)
    for i in range(0, (length/16)+1):
        nonce = "\x00" * 8 + pack(i)
        keystr += aes.encrypt(nonce)
    
    return keystr


def encrypt_ctr(plain, key):
    keystr = keystream(key, len(plain))
    cipher = xor(plain, keystr)
    return cipher


def decrypt_ctr(cipher, key):
    keystr = keystream(key, len(cipher))
    plain = xor(cipher, keystr)
    return plain


def edit(ciphertext, key, offset, newtext):
    plain = decrypt_ctr(ciphertext, key)

    plain = plain[:offset] + newtext
    return encrypt_ctr(plain, key)

def main():
    key = "YELLOW SUBMARINE"

    with open("crypto25.txt", "r") as f:
        content = base64.b64decode(f.read().strip())
        
    aes = AES.new(key, AES.MODE_ECB)
    content = aes.decrypt(content)
    cipher = encrypt_ctr(content, key)

    if len(sys.argv) == 1:
        print cipher.encode('hex')

    elif len(sys.argv) == 3:
        offset = int(sys.argv[1])
        newtext = sys.argv[2]

        print edit(cipher, key, offset, newtext).encode('hex')
    else:
        print "{} <offset> <newtext>".format(sys.argv[0])

if __name__ == "__main__":
    main()
