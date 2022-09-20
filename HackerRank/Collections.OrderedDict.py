# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:32:49 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

od = OrderedDict()

for _ in range(int(input())):
    s = input().split()
    a =  ' '.join(s[:-1])
    b = s[-1]
    if a in od:
        od[a] += int(b)
    else:
        od[a] = int(b)
for i in od:
    print(i , od[i])

