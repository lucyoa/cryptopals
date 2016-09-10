#!/usr/bin/env python

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


def main():
    key = "YELLOW SUBMARINE"
    cipher = base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
    
    print decrypt_ctr(cipher, key)
   
    cipher = encrypt_ctr("Nice 1, testing my encryption", key)
    print cipher.encode('hex')

    print "Decryption..."
    print decrypt_ctr(cipher, key)


if __name__ == "__main__":
    main()
