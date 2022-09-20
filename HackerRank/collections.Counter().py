# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:27:59 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
a = [int(a) for a in input().split()]
c = Counter(a)
n = int(input())
s = 0
for _ in range(n):
    y , z = map(int , input().split())
    if c[y]:
        c[y] -= 1
        s += z
print(s)
        
    
    
