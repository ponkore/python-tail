#!/usr/bin/env python

import argparse
import tail


def print_line(txt):
    print(txt.rstrip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename", type=str)
    args = parser.parse_args()
    #
    filename = args.filename
    t = tail.Tail(filename, encoding='cp932')
    t.register_callback(print_line)
    t.follow(s=1)


main()
