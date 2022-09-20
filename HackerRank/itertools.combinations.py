# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:23:58 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a , b = input().split()
a = sorted(a)
for i in range(1 , int(b) + 1):
    for j in combinations(a , i):
        print(''.join(j))
    

