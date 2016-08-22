#!/usr/bin/env python

def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))

    return res

def main():
    s1 = "1c0111001f010100061a024b53535009181c".decode('hex')
    s2 = "686974207468652062756c6c277320657965".decode('hex')

    print xor(s1, s2).encode('hex')

if __name__ == "__main__":
    main()
