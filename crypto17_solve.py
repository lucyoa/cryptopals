#!/usr/bin/env python

import sys
import subprocess


def crypto17(cipher):
    c = "./crypto17.py {}".format(cipher.encode('hex'))
    process = subprocess.Popen(c.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))
    return res


def main():
    cipher = sys.argv[1].decode('hex')

    solution = ""

    print "Starting..."
    for block in range((len(cipher)/16), 1, -1):
        num = 1
        tmp = ""
        size = len(cipher) - 16

        print "Hacking block: {}".format(block)

        while num < 17:
            i = 0
            while i < 256:
                ch = chr(ord(cipher[size-num]) ^ i ^ num)
                rest = xor(xor(tmp, cipher[size-num+1:size]), (chr(num) *(num-1)))
                payload = cipher[:size-num] + ch + rest + cipher[size:]

                res = crypto17(payload)
                if "Bad padding" not in res:
                    tmp = chr(i) + tmp 
                    print "{} ({})".format(repr(tmp), tmp.encode('hex'))
                    break

                i += 1

                if i == 256:
                    print "Rollback..."
                    i = ord(tmp[-1]) + 1
                    tmp = tmp[:-1]
                    num = num - 1

            num += 1
        solution = tmp + solution
        cipher = cipher[:-16]
    print "FOUND!"
    print "plain: {}".format(solution)
    print "hex: {}".format(solution.encode('hex'))


if __name__ == "__main__":
    main()
