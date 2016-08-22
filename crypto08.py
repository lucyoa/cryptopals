#!/usr/bin/env python


def main():
    with open("crypto08.txt") as f:
        lines = f.readlines()

    best = 0
    for line in lines:
        line = line.strip()
        blocks = [line[i:i+32] for i in range(0, len(line), 32)]

        same = 0
        for i in range(0, len(blocks)-1):
            if blocks[i] in blocks[i+1:]:
                same +=1

        if same > 0:
            print line

if __name__ == "__main__":
    main()
