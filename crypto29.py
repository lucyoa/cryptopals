#!/usr/bin/env python

import sys
import struct


def padSHA1(s):
    b = ""
    for p in s:
        b += '{0:08b}'.format(ord(p))
    ml = len(b)
    bits = b + "1"
    while len(bits) % 512 != 448:
        bits += "0"
    bits += '{0:064b}'.format(ml)

    res = ""
    for chunk in [bits[i:i+8] for i in range(0, len(bits), 8)]:
        res += chr(int(chunk, 2))
    return res


def sha1(plain, h0=0x67452301, h1=0xEFCDAB89, h2=0x98BADCFE, h3=0x10325476, h4=0xC3D2E1F0, length=None):
    def rol(n ,b):
        return ((n << b) | (n >> (32 -b))) & 0xffffffff

    b = ""
    for p in plain:
        b += '{0:08b}'.format(ord(p))

    if length is None:
        ml = len(b)
    else:
        ml = length

    # append the bit '1' to the message e.g
    bits = b + "1"

    # append 0 <= k < 512 bits '0', such that the resulting message length in bits is congruent to -64 = 448 (mod 512)
    while len(bits) % 512 != 448:
        bits += "0"

    # append ml, in a 64-bit big-endian integer. Thus, the total length is multiple of 512 bits
    bits += '{0:064b}'.format(ml)

    for ch in range(0, len(bits) / 512):
        chunk = bits[ch*512:ch*512+512]

        w = [0] * 80

        for i in range(0, 16):
            w[i] = int(chunk[i*32:i*32+32], 2)

        # extend the sixteen 32-bit words into eighty 32-bit words
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)

        # initialize hash value for this chunk
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # Main loop:
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i<= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff

            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return ("%08x" * 5) % (h0, h1, h2, h3, h4)


def sign(msg, key):
    return sha1(key + msg)


def verify(msg, signature, key):
    if sha1(key + msg) == signature:
        return True

    return False


def main():
    key = "This is secret key"
    plain = "comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"

    print plain
    signature = sign(plain, key)
    print signature

    # lets forge
    suffix = ';admin=true'

    # brute key length
    for i in range(1, 30):
        msg = padSHA1("A"*i+plain) + suffix
        h = struct.unpack('>5I', signature.decode('hex'))

        forged = sha1(suffix, h[0], h[1], h[2], h[3], h[4], len(msg)*8)
        if verify(msg[i:], forged, key):
            print ("Got it!\n"
                   "Key length: {}\n"
                   "Plain: {}\n"
                   "Plain in hex: {}\n"
                   "Signature: {}\n").format(i, msg[i:], msg[i:].encode('hex'), forged)

if __name__ == "__main__":
    main()
