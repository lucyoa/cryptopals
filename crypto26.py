#!/usr/bin/env python

import struct
import sys
import urllib

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

def func1(s, key):
    plain = "comment1=cooking%20MCs;userdata=" + urllib.quote(s) + ";comment2=%20like%20a%20pound%20of%20bacon"
    return encrypt_ctr(plain, key)

def func2(cipher, key):
    plain = decrypt_ctr(cipher, key)
    print plain

    if ";admin=true" in plain:
        return True

    return False

def main():
    # solution
    # ./crypto26.py -d 15bea626cacc32d3decc6c32077aad15f7de5c91db1e29abbcbf6df7ce9a12254c9beda47c165225b7e88a0380cce8a4aae58e07799b4b67e13c0912a70b8082bbe7bf5bce7f648c5dedf2
    key = "YELLOW SUBMARINE"

    if sys.argv[1] == "-e":
        cipher = func1(sys.argv[2], key)
        print cipher.encode('hex')

    elif sys.argv[1] == "-d":
        if func2(sys.argv[2].decode('hex'), key):
            print "Admin"
        else:
            print "Noob"

if __name__ == "__main__":
    main()
