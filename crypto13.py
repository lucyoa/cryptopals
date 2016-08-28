#!/usr/bin/env python

# lucyoa@sarge~/git/cryptopals $ ./crypto13.py -decrypt 1452bbfe8ce79865ebc42edbe980914208e1521cde8f4cfd2fc509778942969d61f8e71181fdadf573bf49d5efcdf88560fa36707e45f499dba0f25b922301a5
# email=AAAAAAAAAAAAA&uid=10&role=admin&uid=10&rol
#

import sys
from Crypto.Cipher import AES
from urllib import urlencode

def profile_for(email):
    user = [("email", email),
            ("uid", 10),
            ("role", "user")]
    
    return urlencode(user)

def pad(s):
    num = 16 - (len(s) % 16)
    res = s + chr(num) * num
    return res

def unpad(s):
    num = ord(s[-1])
    return s[:len(s) - num]

def encrypt(plain, key):
    plain = pad(plain)
    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(plain)

    return cipher

def decrypt(cipher, key):
    aes = AES.new(key, AES.MODE_ECB)
    plain = aes.decrypt(cipher)
    return unpad(plain)

def usage():
    print ("Usage:\n"
           "./crypto13 -encrypt mail\n"
           "./crypto13 -decrypt cipher\n")
 
def main():
    randomkey = "YELLOW SUBMARINE"

    if len(sys.argv) != 3:
        usage()
        return

    if sys.argv[1] == "-encrypt":
        profile = profile_for(sys.argv[2])
        cipher = encrypt(profile, randomkey)
        print cipher.encode('hex')
    elif sys.argv[1] == "-decrypt":
        plain = decrypt(sys.argv[2].decode('hex'), randomkey)
        print plain
    else:
        usage()
        return

if __name__ == "__main__":
    main()
