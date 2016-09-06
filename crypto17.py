#!/usr/bin/env python

import sys
import random
import base64
from Crypto.Cipher import AES


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))
    return res


def pad(s):
    num = 16 - (len(s) % 16)
    res = s + chr(num) * num
    return res


def unpad(s):
    print s.encode('hex')
    num = ord(s[-1])
    if num > 16 or s[len(s)-num:] != num * chr(num):
        print 'Bad padding'
        sys.exit(-1)

    return s[:len(s) - num]


def encrypt_ecb(plain, key):
    aes = AES.new(key, AES.MODE_ECB)
    res = aes.encrypt(plain)
    return res 

def decrypt_ecb(cipher, key):
    aes = AES.new(key, AES.MODE_ECB)
    res = aes.decrypt(cipher)
    return res


def encrypt_cbc(plain, key, IV):
    plain = pad(plain)

    cipher = ""
    tmp = IV
    for i in range(0, len(plain) / 16):
        cipher += encrypt_ecb(xor(tmp, plain[i*16:i*16+16]), key)
        tmp = cipher[i*16:i*16+16]

    return IV + cipher


def decrypt_cbc(cipher, key, IV):
    plain = ""
    tmp = IV

    for i in range(0, len(cipher) / 16):
        plain += xor(decrypt_ecb(cipher[i*16:i*16+16], key), tmp)
        tmp = cipher[i*16:i*16+16]

    return unpad(plain)


def random_bytes(num):
    res = ""
    with open('/dev/random') as f:
        res = f.read(num)
    return res


def func1(key):
    iv = random_bytes(16)
    msgs = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
            "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
            "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
            "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
            "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
            "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
            "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
            "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
            "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
            "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]

    i = random.randint(0, len(msgs)-1)
    
    cipher = encrypt_cbc(base64.b64decode(msgs[i]), key, iv)
    return cipher

def func2(cipher, key):
    iv = cipher[:16]
    cipher = cipher[16:]

    plain = decrypt_cbc(cipher, key, iv)
    print plain
    return

def main():
    key = "YELLOW SUBMARINE"

    if len(sys.argv) != 2:
        print func1(key).encode('hex')
    else:
        func2(sys.argv[1].decode('hex'), key)

if __name__ == "__main__":
    main()
