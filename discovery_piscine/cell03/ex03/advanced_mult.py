#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print('none')
else:
    i = 0
    j = 0
    while i < 11:
        j=0
        lst = []
        while j < 11:
            lst.append(j*i)
            j+=1
        print(f'Table de {i}:{lst}')
        i+=1



