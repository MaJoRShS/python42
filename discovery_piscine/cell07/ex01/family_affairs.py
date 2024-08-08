#!/usr/bin/env python3
# your method definition here
# ----------------------            First Implementation         --------------------------

def find_the_redheads(arg):
    k = []
    for key, value in arg.items():
        if value == "red":
            k.append(f'{key}')
    return k


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

# -----------------------------------------------------------------------------------------