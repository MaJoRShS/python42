#!/usr/bin/env python3

import sys

print(sys.argv)
lst = []
for n in range(int(sys.argv[1]), int(sys.argv[2])+1,1):
    lst.append(n)
print(lst)