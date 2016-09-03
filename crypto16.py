#!/usr/bin/env python

import urllib
import sys
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

    try:
        if s[len(s)-num:] != num * chr(num):
            raise Exception('Bad padding')
    except Exception as e:
        return e

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


def func1(s, key):
    iv = random_bytes(16)
    plain = "comment1=cooking%20MCs;userdata=" + urllib.quote(s) + ";comment2=%20like%20a%20pound%20of%20bacon"
    return encrypt_cbc(plain, key, iv)


def func2(s, key):
    iv = s[:16]
    cipher = s[16:]

    plain = decrypt_cbc(cipher, key, iv)
    print plain

    if ";admin=true;" in plain:
        return True

    return False


def main():
    key = "YELLOW SUBMARINE"

#   break it
#   print xor(xor("817e3a6873dbf3282495aa0f406b41fd".decode('hex'), "0of%20bacon\x05\x05\x05\x05\x05"), ";admin=true;\x04\x04\x04\x04").encode('hex')
#   ./crypto16.py -d 0b43019112f669ca1d38114602ae9958cbb3170582d861fb42275455ef5d693adc450da12ffa21fed29c52cdf1c171215022b7e835eb5cbf6e070ce114e82de88a7038202885ac3d358fa131416a40fcbb397a7ecae4b4db94242316a6e44335

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
