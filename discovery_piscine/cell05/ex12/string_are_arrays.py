#!/usr/bin/env python3
import sys

contador= 0
if len(sys.argv) >= 1:
    str = list(sys.argv[1])
    size = len(str)
    for i in range(size):
        if str[i] == 'z':
            contador+=1    
    print(contador*'z')
