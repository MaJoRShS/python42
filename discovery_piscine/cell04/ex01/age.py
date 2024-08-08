#!/usr/bin/env python3
age = int(input('Please tell me your age: '))

init = 0
max = 3

print(f'You are currently {age} years old.')
newAge = age
while init < max:
    print(f'In {init+1}0 years, you\'ll be {newAge+10} years old. ')
    newAge = newAge+10
    init+=1


