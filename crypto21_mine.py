#!/usr/bin/env python


class mt19937(object):
    MT = []
    index = 0

    def __init__(self, seed):
        self.MT.append(seed)

        for i in range(1, 624):
            self.MT.append(((1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i) & 0xffffffff))


    def extractNumber(self):
        if self.index == 0:
            self.generateNumbers()

        y = self.MT[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)
        y = y ^ ((y << 15) & 4022730752)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y

    def generateNumbers(self):
        for i in range(0, 624):
            y = (self.MT[i] & 0x80000000)+ (self.MT[(i+1) % 624] & 0x7fffffff)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)

            if y % 2 == 1:
                self.MT[i] = self.MT[i] ^ 2567483615


def main():
    rnd = mt19937(123)
    print rnd.extractNumber()

if __name__ == "__main__":
    main()
