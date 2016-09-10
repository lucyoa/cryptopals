#!/usr/bin/env python

import base64
from Crypto.Cipher import AES


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))
    return res


def keystream(key, length):
    keystr = ""
    nonce = "\x00" * 16
    aes = AES.new(key, AES.MODE_ECB)

    for i in range(0, (length / 16) + 1):
        keystr += aes.encrypt(nonce)
    
    return keystr


def encrypt_ctr(plain, key):
    keystr = keystream(key, len(plain))
    cipher = xor(plain, keystr)

    return cipher


def decrypt_ctr(cipher, key):
    keystr = keystream(key, len(cipher))
    cipher = xor(cipher, keystr)

    return plain


def main():
    with open("crypto20.txt", "r") as f:
        lines = f.readlines()

    key = "YELLOW SUBMARINE"
    for line in lines:
        line = base64.b64decode(line.strip())
        print encrypt_ctr(line, key).encode('hex')


if __name__ == "__main__":
    main()
