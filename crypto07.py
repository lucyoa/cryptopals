#!/usr/bin/env python

import base64
from Crypto.Cipher import AES

def main():
    with open("crypto07.txt") as f:
        content = base64.b64decode(f.read().strip())

    aes = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
    print aes.decrypt(content)

if __name__ == "__main__":
    main()
