#!/usr/bin/env python


def xor(s1, s2):
    l = len(s1)
    if l < len(s2):
        l = len(s2)

    res = ""
    for i in range(0, l):
        res += chr(ord(s1[i % len(s1)]) ^ ord(s2[i % len(s2)]))
    return res

def main():
    s = ("Burning 'em, if you ain't quick and nimble\n"
         "I go crazy when I hear a cymbal")

    print xor(s, "ICE").encode('hex')


if __name__ == "__main__":
    main()
