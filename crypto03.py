#!/usr/bin/env python


alph = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

def score(s1):
    score = 0
    for i in range(0, len(s1)):
        letter = s1[i].lower()
        if letter in alph.keys():
            score += alph[letter]
    return score

def xor(s1, s2):
    l = len(s1)
    if l < len(s2):
        l = len(s2)

    res = ""
    for i in range(0, l):
        res += chr(ord(s1[i % len(s1)]) ^ ord(s2[i % len(s2)]))
    return res

def main():
    s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')

    best = 0
    solve = None
    for i in range(0, 0xff):
        res = xor(s1, chr(i))
        s = score(res)
        if s > best:
            best = s
            solve = chr(i)

    print xor(s1, solve)

if __name__ == "__main__":
    main()

