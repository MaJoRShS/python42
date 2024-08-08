#!/usr/bin/env python3
import sys

size =len(sys.argv) 
i=1
print(f'parameters: {len(sys.argv) -1 }')

while i < size:
    print(f'{sys.argv[i]}: {len(sys.argv[i])}')
    i+=1



# if len(sys.argv) == 1:
#     print(sys.argv)
#     print('none')