#!/usr/bin/env python3
import sys

arg = sys.argv

# if len(arg) <= 2:
#     print('none')
# else:
reverse = arg[::-1]

# print(arg.reverse())
# print(list(reversed(arg)))
# print(reverse, end="")

for i in range(len(reverse)-1):
    print(reverse[i])