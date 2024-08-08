#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

new = filter(lambda x: x > 5,arr)
new = map(lambda x: x + 2,new)
print(arr)
print(list(set(new)))