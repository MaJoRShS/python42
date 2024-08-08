#!/usr/bin/env python3
number = input()


if int(number) == 0:
    print('This number is both positive and negative.')
if int(number) >= 0:
    print('This number is positive.')
if int(number) < 0:
    print('This number is negative.')
