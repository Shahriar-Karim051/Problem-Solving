# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 03:06:24 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s , k = input().split()
s = sorted((s))
c = list(permutations(s , int(k)))
#print(c)
for i in c:
    print("".join(i))

    



#print("/n".join(c))