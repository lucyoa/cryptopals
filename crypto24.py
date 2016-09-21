#!/usr/bin/env python

import random
import struct
import time


class mt19937(object):
    def __init__(self, seed):
        self.MT = []
        self.index = 0

        self.MT.append(seed)

        for i in range(1, 624):
            self.MT.append(((1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i) & 0xffffffff))

    def extractNumber(self):
        if self.index == 0:
            self.generateNumbers()

        y = self.MT[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)
        y = y ^ ((y << 15) & 4022730752)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y

    def generateNumbers(self):
        for i in range(0, 624):
            y = (self.MT[i] & 0x80000000)+ (self.MT[(i+1) % 624] & 0x7fffffff)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)

            if y % 2 == 1:
                self.MT[i] = self.MT[i] ^ 2567483615


class mt19937cipher(object):
    def xor(self, s1, s2):
        res = ""
        for i in range(0, len(s1)):
            res += chr(ord(s1[i]) ^ ord(s2[i]))

        return res


    def encrypt(self, plain, key):
        rng = mt19937(key)
        keystream = ""

        for i in range(0, len(plain) / 4 + 1):
            keystream += struct.pack("<L", rng.extractNumber())

        cipher = self.xor(plain, keystream)
        return cipher


    def decrypt(self, cipher, key):
        return self.encrypt(cipher, key)


def main():
    print "Write the function that does this for MT19937 using a 16-bit seed. Verify that you can encrypt and decrypt properly. This code should look similar to your CTR code."
    plain = "Test this avesome string"
    key = random.getrandbits(16)

    print "Encrypting..."
    cipher = mt19937cipher().encrypt(plain, key)
    print cipher.encode('hex')

    print "Decrypting..."
    plain = mt19937cipher().decrypt(cipher, key)
    print plain

    print "Use your function to encrypt a known plaintext (say, 14 consecutive 'A' characters) prefixed by a random number of random characters."
    char = chr(random.randint(0, 0xff))
    num = int(random.randint(0, 100))

    plain = char * num + "A" * 14
    cipher = mt19937cipher().encrypt(plain, key)
    print cipher.encode('hex')

    print "From the ciphertext, recover the \"key\" (the 16 bit seed)."
    known = "A" * 14

    res = mt19937cipher().xor(cipher, "A" * len(cipher))
    print  res.encode('hex')
    print key

    try:
        for key in range(0, 256*256):
            rng = mt19937(key & 0xffff)
            keystream = ""
            for i in range(0, len(cipher) / 4 + 1):
                keystream += struct.pack("<L", rng.extractNumber())

            for j in range(0, len(res)-8):
                tmp = res[j:j+8]

                if tmp in keystream:
                    raise Exception
    except:
        print "Found seed: {}".format(key)

    print "Use the same idea to generate a random \"password reset token\" using MT19937 seeded from the current time."
    char = chr(random.randint(0, 0xff))
    num = int(random.randint(0, 100))
    
    plain = char * num + "A" * 14

    key = int(time.time())
    print "Key: {}".format(key)

    cipher = mt19937cipher().encrypt(plain, key)
    print cipher.encode('hex')

    print "Write a function to check if any given password token is actually the product of an MT19937 PRNG seeded with the current time."

    timestamp = int(time.time())
    offset = 3600

    res = mt19937cipher().xor(cipher, "A" * len(cipher))

    try:
        for k in range(timestamp - offset, timestamp+1):
            rng = mt19937(timestamp)

            keystream = ""
            for i in range(0, len(cipher) / 4 + 1):
                keystream += struct.pack("<L", rng.extractNumber())

            for j in range(0, len(res)-8):
                tmp = res[j:j+8]

                if tmp in keystream:
                    raise Exception
    except:
        print "Found seed: {}".format(k)


if __name__ == "__main__":
    main()
