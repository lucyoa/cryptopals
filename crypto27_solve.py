#!/usr/bin/env python

import subprocess


def cmd(c):
    process = subprocess.Popen(c.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out


def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i]))
    return res


def main():
    payload = "244c0159144b81ff88b66d9d0eff13eb5752937b3a7bd1fb3b2f570eaff538c196c713ecce0ee10aeb8bb3fbd599096624b35578bdb9fd15e0cddc2ee8f1348febc7e73233e250c77ee7eb0c1a8bd6b0".decode('hex')
    plain = cmd("./crypto27.py -d " + payload.encode('hex')).split("\n")[0]

    s1 = plain[16:32]
    s2 = payload[:16]

    res = xor(s1, s2)

    payload = payload[16:]

    plain = cmd("./crypto27.py -d " + payload.encode('hex')).split("\n")[0]
    s1 = plain[:16]

    key = xor(res, s1)
    print "The key is: {}".format(key)


if __name__ == "__main__":
    main()
