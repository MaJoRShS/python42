#!/usr/bin/env python3
lessThan25 = int(input('Enter a number less than 25 \n'))
if lessThan25 >= 25:
    print('Error')
else:
    while lessThan25 < 26:
        print(f'Inside the loop, my variable is {lessThan25}')
        lessThan25+=1