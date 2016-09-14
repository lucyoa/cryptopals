#!/usr/bin/env python


def _int32(x):
    return int(0xffffffff & x)


class MT19937(object):
    def __init__(self, seed):
        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed

        for i in range(1, 624):
            self.mt[i] = _int32(1812433253 * (self.mt[i-1] ^ self.mt[i-1] >> 30) + i)

    def rand(self):
        if self.index >= 624:
            self.twist()

        y = self.mt[self.index]

        # Right shift by 11 bits
        y = y ^ y >> 11
        # Shift y left by 7 and take the bitwise and of 2636928640
        y = y ^ y << 7 & 2636928640
        # Shift y left by 15 and take the bitwise and of y and 4022730752
        y = y ^ y << 15 & 4022730752
        # Right shift by 18 bits
        y = y ^ y >> 18

        self.index = self.index + 1

        return _int32(y)

    def twist(self):
        for i in range(624):
            # Get the most significat bit and add it to the less significant
            # bits of the next number

            y = _int32((self.mt[i] & 0x80000000) +
                       (self.mt[(i+1) % 624] & 0x7fffffff))
            self.mt[i] = self.mt[(i+397) % 624] ^ y >> 1

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df

        self.index = 0


def main():
    rnd = MT19937(123)
    print rnd.rand()

if __name__ == "__main__":
    main()
