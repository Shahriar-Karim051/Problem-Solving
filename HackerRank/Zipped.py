# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:13:27 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a , b = map(int , input().split())
l = []
for _ in range(b):
    c = [float(c) for c in input().split()]
    l.append(c)
print(*[sum(i) / len(i) for i in zip(*l)] , sep = '\n')