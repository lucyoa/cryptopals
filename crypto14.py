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
    rand_prefix = "YELLOW SUBMARINADSADSAKHDSKAHDSKJAHDSKAJ"

    # detect bytes left to 16-byte block
    s = -1
    for i in range(0, 256):
        my = "A" * i
        cipher = encrypt_ecb(rand_prefix + my + unknown, key)
        for j in range(0, len(cipher)/16):
            if cipher[j*16:j*16+16] == cipher[j*16+16:j*16+32]:
                s = i % 16 
                poz = j - 1
                break
        if s != -1:
            break

    # now break it - byte-at-a-time
    solution = ""
    size = 256
    for num in range(size - 1, 0, -1):
        my =  "B" * s+ "A" * num
        cipher = encrypt_ecb(rand_prefix + my + unknown, key)

        for i in range(0, 256):
            my = "B" * s + "A" * num + solution + chr(i)
            guess = encrypt_ecb(rand_prefix + my + unknown, key)

            if guess[size+poz*16:size+poz*16+16] == cipher[size+poz*16:size+poz*16+16]:
                solution += chr(i)
                break

    print solution

if __name__ == "__main__":
    main()
