#!/usr/bin/env python

def unpad(s):
    num = ord(s[-1])

    try:
        if s[len(s)-num:] != num * chr(num):
            raise Exception('Bad padding')
    except Exception as e:
        return e

    return s[:len(s) - num]

def main():
    print unpad("ICE ICE BABY\x04\x04\x04\x04")
    print unpad("ICE ICE BABY\x05\x05\x05\x05")
    print unpad("ICE ICE BABY\x01\x02\x03\x04")

if __name__ == "__main__":
    main()
