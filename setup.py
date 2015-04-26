#! /usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='CLI Java Editor',
    version='0.0.1',
    author='Sam Elkhateeb',
    author_email='same@nanosn.com',
    description='A command-line interface for editing Java projects.',
    license='BSD',
    keywords='java editor',
    url='http://packages.python.org/je',
    packages=['java'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Topic :: Utilities',
        'License :: BSD License',
    ],
    entry_points={
        'console_scripts': [
            'je = java.je:main',
        ],
    },
)
