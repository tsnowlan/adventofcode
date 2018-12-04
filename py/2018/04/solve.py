#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', default='input.txt', help='input data')
    parser.add_argument('--verbose', action='store_true', help="be extra chatty")
    parser.add_argument('--debug', action='store_true', help="run in debug mode")
    args = parser.parse_args()

    if args.debug:
        setattr(args, 'verbose', True)

    # do something


###


if __name__ == '__main__':
    main()
