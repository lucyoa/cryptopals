#!/usr/bin/env python

import base64

def main():
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d".decode('hex')
    print base64.b64encode(s)

if __name__ == "__main__":
    main()
