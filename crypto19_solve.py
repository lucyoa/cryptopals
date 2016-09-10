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
    ' ': 0.1918182,
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
    ciphers = ["3ff1a32ad9c7668f86db23290476ae5217a5eb28c3cd3587c3c0657d0872ba",
               "35bea622c1c566958adb6b7d1a7ab51b12f1ad2accc735",
               "30a3a4268fc129978ddb662f4c7cb15212b4b8208fc32b8d8dc8233a1e76ba",
               "33b8ac23dbc7238c97c72e3e097db70704a8eb23c0d735879081",
               "3ff1a32ad9c7669282dc70380833b41b02b9eb2a8fcc2986c3c0657d187ba6521eb4aa2f",
               "39a3eb3bc0ce2f96868f6e380d7daa1c11bdae38dc82318d91cb7071",
               "39a3eb23ced423c28fc66d3a0961a61656b0bc23c6ce23c282c1677d1f72aa16",
               "26bea722dbc7668f86ce6d340274af1705a2eb3cc0d02291cf",
               "37bfaf6bdbca299784c7777d0e76a51d04b4eb028fca2786c3cb6c3309",
               "39b7eb2a8fcf298188c66d3a4c67a21e13f1a4398fc366858acd66",
               "22beeb3bc3c72791868f627d0f7cae0217bfa224c1",
               "37a3a43ec1c666968bca233b0561a65217a5eb3fc7c766818fda6171",
               "34b4a225c882258791db62340233b71a17a5eb3fc7c73fc282c1677d25",
               "34a4bf6bc3cb3087878f74350961a6521bbebf27cadb668b908f74321e7df9",
               "37bda76bccca278c84ca67714c70ab1318b6ae2f8fd7329686dd6f2456",
               "37f1bf2eddd02f808fca233f0972b6060ff1a2388fc029908d81",
               "22b9aa3f8fd5298f82c1242e4c77a20b05f1bc2eddc7669193ca6d29",
               "3fbfeb22c8cc299082c1777d0b7cac1656a6a227c38e",
               "3eb4b96bc1cb218a97dc23340233a20011a4a62ec1d6",
               "23bfbf22c3822e87918f75320570a65211a3ae3c8fd12e908ac36f73",
               "21b9aa3f8fd4298b80ca23300361a65205a6ae2edb82328a82c123350961b0",
               "21b9ae258fdb29978dc8233c0277e31013b0be3fc6c4338ecf",
               "25b9ae6bddcd2287c3db6c7d0472b1001fb4b93890",
               "22b9a2388fcf278cc3c762394c78a60202f1aa6bdcc12e8d8cc3",
               "37bfaf6bddcd2287c3c0762f4c64aa1c11b4af6bc7cd34918681",
               "22b9a2388fcd328a86dd23350560e31a13bdbb2edd82278c878f652f0576ad16",
               "21b0b86bcccd2b8b8dc823340267ac521eb8b86bc9cd34818694",
               "3eb4eb26c6c52e96c3c7622b0933b41d18f1ad2ac2c7668b8d8f77350933a61c12fd",
               "25beeb38cacc358b97c675384c7baa0156bfaa3fdad023c290ca66300977ef",
               "25beeb2fced02f8c848f62330833b00513b4bf6bc7cb35c297c76c280b7bb75c",
               "22b9a2388fcd328a86dd23300d7de33b56b9aa2f8fc6348782c26639",
               "37f1af39dacc2d878d83232b0d7aad5f11bda439c6cd3391c3c36c28183d",
               "3eb4eb23cec666868cc1667d017cb00656b3a23fdbc734c294dd6c330b",
               "22beeb38c0cf23c294c76c7d0d61a65218b4aa398fcf3fc28bca622f183f",
               "2fb4bf6be68228978ecd662f4c7baa1f56b8a56bdbca23c290c06d3a57",
               "3eb4e76bdbcd29cec3c7622e4c61a6011fb6a52ecb822e8b908f733c1e67",
               "3fbfeb3fc7c7668182dc763c0033a01d1bb4af3294",
               "3eb4e76bdbcd29cec3c7622e4c71a61718f1a823cecc2187878f6a334c7baa0156a5be39c18e",
               "22a3aa25dcc429908eca677d1967b71704bdb271",
               "37f1bf2eddd02f808fca233f0972b6060ff1a2388fc029908d81"]

    lines = []

    for i in range(0, 16):
        line = ""
        for cipher in ciphers:
            cipher = cipher.decode('hex')
            line += cipher[i]
        lines.append(line)
        
    # break
    keystr = ""
    for line in lines:
        best = 0
        solve = None
        for i in range(0, 256):
            res = xor(line, chr(i))
            s = score(res)

            if s > best:
                best = s
                solve = chr(i)

        keystr += solve
    
    for cipher in ciphers:
        cipher = cipher.decode('hex')
        print xor(cipher, keystr)

if __name__ == '__main__':
    main()
