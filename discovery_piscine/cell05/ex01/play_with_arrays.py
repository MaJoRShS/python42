#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]

new = map(lambda x: x+2,arr)
print(f'Original array: {arr}')
print(f'New array: {list(new)}')