#!/usr/bin/env python3
# import sys

# if len(sys.argv) == 1:
#     print('none')

# i=0
# size = len(sys.argv)
# for i in range(size-1):
#     i+=1
#     if "ism" in sys.argv[i]:
#         pass
#     else:
#         sys.argv[i]+="ism"
#         # print(sys.argv[i])
#         print(f'{sys.argv[i]}')

#--------------------------------------------------------------------------

#new
import sys

match len(sys.argv):
    case 1:
        print('none')

size = len(sys.argv)
for i in range(1, size):
    match sys.argv[i]:
        case _ if "ism" in sys.argv[i]:
            pass
        case _:
            sys.argv[i] += "ism"
            print(sys.argv[i])
