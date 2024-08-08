#!/usr/bin/env python3
# Your method definition
import sys

arg = sys.argv

def downcase_it(arg):
    return arg.lower()

size = len(arg)
if size <= 1:
    print(None)
else:
    for i in range(1,size):
        print(downcase_it(arg[i]))

