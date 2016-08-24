#!/usr/bin/env python

def pad(x, blocksize):
    num = blocksize - (len(x) % blocksize)
    res = x + chr(num) * num
    return res

def main():
    s = "YELLOW SUBMARINE"
    print pad(s, 20).encode('hex')

if __name__ == "__main__":
    main()
