# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 02:51:53 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]
c = list(product(a , b))
print(*c)