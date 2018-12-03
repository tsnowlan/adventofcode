#!/usr/bin/env python

import argparse
from collections import Counter


UNCLAIMED = '.'
CLAIMED = "#"
SHARED = "X"


class Fabric(object):
    def __init__(self, cols=1000, rows=1000):
        self.rows = rows
        self.cols = cols
        self._map = [['.' for y in range(rows+1)] for x in range(cols+1)]

    def pos(self, i, j):
        return self._map[i][j]

    def claim(self, origin, shape="1x1"):
        i_min, j_min = [int(x) for x in origin.split(",")]
        cols, rows = [int(x) for x in shape.split("x")]
        i_max = i_min + cols
        j_max = j_min + rows
        for i in range(i_min, i_max):
            for j in range(j_min, j_max):
                if self.pos(i, j) == UNCLAIMED:
                    self._map[i][j] = CLAIMED
                elif self.pos(i, j) == CLAIMED:
                    self._map[i][j] = SHARED

    def print_map(self):
        print()
        for j in range(self.cols):
            row_str = ""
            for i in range(self.rows):
                row_str += self.pos(i, j)
            print(row_str+"")
        print()

    @property
    def total_shared(self):
        return sum([sum([1 for y in x if y == SHARED]) for x in self._map])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='input.txt', help='input data')
    parser.add_argument('--area', '-a', action='store_true', help='solve for overlap area')
    parser.add_argument('--verbose', action='store_true', help="be extra chatty")
    parser.add_argument('--debug', action='store_true', help="run in debug mode")
    args = parser.parse_args()

    cols = 1000
    rows = 1000

    if args.debug:
        setattr(args, 'verbose', True)
        rows = cols = 10
        args.input = 'debug_input.txt'

    fab = Fabric(cols, rows)
    with open(args.input) as infile:
        for line in infile:
            req_id, _, origin, shape = line.strip().replace(':', '').split(' ')
            fab.claim(origin, shape)
    if args.debug:
        fab.print_map()
    print(F"Total shared: {fab.total_shared}")


###


if __name__ == '__main__':
    main()
