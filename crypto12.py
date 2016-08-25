#!/usr/bin/env python

import base64
from Crypto.Cipher import AES


def pad(s):
    num = 16 - (len(s) % 16)
    res = s + chr(num) * num
    return res


def encrypt_ecb(plain, key):
    plain = pad(plain)

    aes = AES.new(key, AES.MODE_ECB)
    cipher = aes.encrypt(plain)
    return cipher


def main():
    unknown = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
                               "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
                               "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
                               "YnkK")

    # random key
    key = "YELLOW SUBMARINE"

    solution = ""
    size = 256
    for num in range(size - 1, 0, -1):
        my = "A" * num
        cipher = encrypt_ecb(my + unknown, key)

        for i in range(0, 255):
            my = "A" * num + solution + chr(i)
            guess = encrypt_ecb(my + unknown, key)

            if guess[size-16:size] == cipher[size-16:size]:
                solution += chr(i)
                break

    print solution

if __name__ == "__main__":
    main()
