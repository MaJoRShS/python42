#!/usr/bin/env python3
import sys

arg = sys.argv

ls = list(arg)

def shrink(arg):
    # aqui só exibe as 8 primeiras letras de cada item
    return arg[:8]


def enlarge(arg):
    # aqui tem que colocar a letra Z até completar 8 posições
    while len(ls[0]) <= 8:
        ls[0]+="Z"
    return ls[0]

if len(ls) == 1:
    print(None)
else:
    ls.pop(0)
    for i in range(len(ls)):
        if len(ls[i]) < 8:
            print(enlarge(ls[i]))
        else:
            print(shrink(ls[i]))