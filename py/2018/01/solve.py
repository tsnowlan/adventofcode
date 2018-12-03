#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='input.txt', help="input data")
    parser.add_argument('--sum', '-s', action='store_true', help="get final sum freq")
    parser.add_argument('--dupe', '-d', action='store_true', help='get first duplicated freq')
    parser.add_argument('--verbose', action='store_true', help="be extra chatty")
    parser.add_argument('--debug', action='store_true', help="run in debug mode")
    args = parser.parse_args()

    if args.debug:
        setattr(args, 'verbose', True)

    if not args.sum ^ args.dupe:
        raise Exception("You must specify either --sum/-s or --dupe/-d")

    freqs = {"sum": 0, "seen": set()}
    while 1:
        with open(args.input) as infile:
            for line in infile:
                freqs["sum"] += int(line)
                if args.dupe and freqs["sum"] in freqs["seen"]:
                    print(F"First dupe freq: {freqs['sum']}")
                    return
                freqs["seen"].add(freqs["sum"])
            if args.sum:
                break
    print(F"Final freq: {freqs['sum']}")


###


if __name__ == '__main__':
    main()
