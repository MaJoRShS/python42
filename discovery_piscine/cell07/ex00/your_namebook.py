#!/usr/bin/env python3

def array_of_names(arg):
    k = []
    for key, value in arg.items():
        k.append(f'{key.capitalize()} {value.capitalize()}')
    return k

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

