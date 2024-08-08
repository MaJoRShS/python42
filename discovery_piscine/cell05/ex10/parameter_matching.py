#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print(sys.argv)
    print('none')

if len(sys.argv) > 1:
    print(sys.argv)
    aa = input('What was the parameter? ')
    if sys.argv[1] == aa:
        print('Good job!')
    else:
        print('Nope, sorry...')