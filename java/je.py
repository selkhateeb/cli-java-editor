#! /usr/bin/env python

'''
CLI Java Editor.
'''

import argparse
import class_finder
import sys

class JavaEditor(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='CLI Java Editor.')
        parser.add_argument('command', help='Command to run.')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)

        getattr(self, args.command)(sys.argv[2:])

    def find(self, args):
        class_finder.main(args)


def main():
    JavaEditor()

if __name__ == '__main__':
    main()
