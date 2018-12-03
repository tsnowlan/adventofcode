#!/usr/bin/env python

import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='input.txt', help='input data')
    parser.add_argument('--checksum', '-c', action='store_true', help='get checksum')
    parser.add_argument('--find', '-f', action='store_true', help='find the correct 2 boxes')
    parser.add_argument('--verbose', action='store_true', help="be extra chatty")
    parser.add_argument('--debug', action='store_true', help="run in debug mode")
    args = parser.parse_args()

    if not args.checksum ^ args.find:
        raise Exception("You must choose either --checksum/-c or --find/-f")

    if args.debug:
        setattr(args, 'verbose', True)

    if args.checksum:
        counts = {3: 0, 2: 0}
        lines = 0
        with open(args.input) as infile:
            for line in infile:
                line = line.strip()
                lines += 1
                mults = set(Counter(line).values())
                for i in mults:
                    if i in counts:
                        counts[i] += 1
                    else:
                        counts[i] = 1
        print(counts[2] * counts[3])
    else:
        ids = []
        with open(args.input) as infile:
            for line in infile:
                ids.append(line.strip())
        ids.sort()

        one_off = []
        for i in range(1, len(ids)):
            diff = -1
            for j in range(len(ids[i])):
                if ids[i][j] != ids[i-1][j]:
                    if diff != -1:
                        diff = -1
                        break
                    diff = j
            if diff != -1:
                print(F"Shared letters: {ids[i][0:diff]}{ids[i][diff+1:]}")


###


if __name__ == '__main__':
    main()
