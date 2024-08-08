#!/usr/bin/env python3
first_value = int(input('Enter the first number: '))
second_value = int(input('Enter the second number: '))

mult = first_value * second_value;

if int(mult) == 0:
    print(f'{first_value} x {second_value} = {mult}')
    print('The result is positive and negative.')
if int(mult) > 0:
    print(f'{first_value} x {second_value} = {mult}')
    print('The result is positive.')
if int(mult) < 0:
    print(f'{first_value} x {second_value} = {mult}')
    print('The result is negative.')

    