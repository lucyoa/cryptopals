#!/usr/bin/env python

import base64
import sys
import random
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
    num = ord(s[-1])
    return s[:len(s) - num]


def encrypt_ecb(plain, key):
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(plain)
    return cipher


def decrypt_ecb(cipher, key):
    aes = AES.new(key, AES.MODE_ECB)
    plain = aes.decrypt(cipher)
    return plain


def encrypt_cbc(plain, key, IV):
    plain = pad(plain)
    
    cipher = ""
    tmp = IV

    for i in range(0, len(plain) / 16):
        cipher += encrypt_ecb(xor(tmp, plain[i*16:i*16+16]), key)
        tmp = cipher[i*16:i*16+16]

    return cipher


def decrypt_cbc(cipher, key, IV):
    plain = ""
    tmp = IV

    for i in range(0, len(cipher) / 16):
        plain += xor(decrypt_ecb(cipher[i*16:i*16+16], key), tmp)
        tmp = cipher[i*16:i*16+16]

    return unpad(plain)


def random_data(length):
    data = ""
    with open('/dev/random', 'r') as f:
        data = f.read(length)
    return data

def oracle(data):
    for i in range(0, len(data) / 16):
        if data[i*16:i*16+16] in data[i*16+16:]:
            return True

def main():
    # my input
    plain = "A"*80
    key = random_data(16)
    IV = random_data(16)

    pick = random.randint(0, 1)
    data = random_data(random.randint(5,10)) + plain + random_data(random.randint(5, 10))
    if pick:
        cipher = encrypt_ecb(pad(data), key)
    else:
        cipher = encrypt_cbc(data, key, IV)

    print "Cipher: " + cipher.encode('hex')
    print "Trying Oracle:"
    if oracle(cipher):
        print "- ECB Mode"
    else:
        print "- CBC Mode"

    print "Veryfing..."
    if pick:
        print "- It was ECB Mode"
    else:
        print "- It was CBC Mode"


if __name__ == "__main__":
    main()
