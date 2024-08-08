#!/usr/bin/env python3
import re
import sys

arg = sys.argv

arg.pop(0)
aa = re.findall(arg[0],arg[1])
print(len(aa))

