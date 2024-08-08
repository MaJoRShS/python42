#!/usr/bin/env python3

f = int(input('Give me the first number: '))
s = int(input('Give me the second number: '))
print('Thank you!')


if s == 0:
    print(f'{f} + {s} = {f+s}')
    print(f'{f} - {s} = {f-s}')
    print(f'{f} / {s} = Undefined')
    print(f'{f} * {s} = {f*s}')
else:
    print(type(f))
    print(type(s))
    print(f'{f} + {s} = {f+s}')
    print(f'{f} - {s} = {f-s}')
    print(f'{f} / {s} = {f//s}')
    #Aqui passando como // ele já vira int automaticamente e não precisa do round();
    print(type(f))
    print(type(s))
    print(f'{f} * {s} = {f*s}')
