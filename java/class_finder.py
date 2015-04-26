#! /usr/bin env python

'''
Assumptions:
 - All projects uses 'git' for SCM
 - 'src/main/java/' is the directory contains src codes.
 - 'src/test/java/' is the directory contains test codes.


TODOs:
 - use git to find base dir.
'''

import argparse
import subprocess
import fnmatch
import re
import os
import sys


class JavaFile(object):
    """Represents a java file.
    """
    source_path = 'src/main/java/'
    tests_path = 'src/test/java/'
    src_pattern = re.compile('.+/src/.+/java/(.+)\.java')

    def __init__(self, path):
        self.path = path

    def qualified_name(self):
        return re.sub(self.src_pattern, r'\1', self.path).replace('/', '.')



def _find_files(re_pattern, path='.'):
    pattern = re.compile(re_pattern)
    matches = []
    for root, dirnames, filenames in os.walk(path):
        matches += [os.path.join(root, f) for f in filenames
                    if pattern.match(os.path.join(root, f))]
    return matches


def find_java_class(class_name_pattern='*', path='.'):
    '''Returns a list of classes that matches class_name_pattern ignoring case.

    class_name_pattern:
     - '*' will be replaced with '.*'
    - [A-Z] any capital letter will be surrounded by '.*'
    '''
    ptrn = class_name_pattern.replace('*', '.*')
    ptrn = re.sub(r'([A-Z])', r'.*\1.*', ptrn)
    return _find_files(re_pattern='.*/src/.+' + ptrn + '.*\.java$', path=path)


# Utilities
# ---------
def git_basedir():
    '''Returns the base directory of a git project.
    '''
    cmd = ['git', 'rev-parse', '--show-toplevel']
    return subprocess.check_output(cmd, universal_newlines=True)[:-1]


def cli_parser(args=sys.argv):
    parser = argparse.ArgumentParser(description='Finds Java classes.')
    parser.add_argument('pattern', type=str, help='Class search pattern.')
    parser.add_argument('--package', action='store_true',
                        help='Show in Java package format.')

    return parser.parse_args(args)

def main(args=sys.argv):
    args = cli_parser(args)
    foo = find_java_class(args.pattern, path=git_basedir())
    if args.package:
        print '\n'.join([JavaFile(f).qualified_name() for f in foo])
    else:
        print '\n'.join([JavaFile(f).path for f in foo])


if __name__ == '__main__':
    main()
