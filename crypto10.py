#!/usr/bin/env python

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
        tmp = cipher

    return cipher


def decrypt_cbc(cipher, key, IV):
    plain = ""
    tmp = IV

    for i in range(0, len(cipher) / 16):
        plain += xor(decrypt_ecb(cipher[i*16:i*16+16], key), tmp)
        tmp = cipher[i*16:i*16+16]

    return unpad(plain)


def main():
    # Testing
    # plain = "Z"*15
    # key = "A"*16
    # IV = "C"*16

    # cipher = encrypt_cbc(plain, key, IV)
    # plain = decrypt_cbc(cipher, key, IV)
    # print plain

    with open("crypto10.txt", "r") as f:
        cipher = base64.b64decode(f.read().strip())

    key = "YELLOW SUBMARINE"
    IV = "\x00" * 16

    print decrypt_cbc(cipher, key, IV)


if __name__ == "__main__":
    main()
