#!/usr/bin/env python3
def greetings(arg = "noble stranger"):
    if isinstance(arg, str):
        return print(f'Hello, {arg}')
    else:
        return print('Error! It was not a name.')

greetings('Alexandra.')
greetings('Wil')
greetings()
greetings(42)