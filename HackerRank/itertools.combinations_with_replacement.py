# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 02:03:07 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

a , b = input().split()
a = sorted(a)
c = list(combinations_with_replacement(a , int(b)))
'''
for i in c:
    print(''.join(i))
'''
print(*[''.join(i) for i in c] , sep = '\n')