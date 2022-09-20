# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:23:57 2021
Problem Code: STICKS
@author: DELL
"""
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = [int(s) for s in input().split()]
    c = Counter(s)
    l = []
    m = []
    h1=h2=-1
    for i in c:
        if c[i] >= 2:
            l.append(i)
        if c[i] >= 4:
            l.append(i)
    if len(m) != 0:
        h1 = max(m)**2
        
    if len(l) > 1:
        l.sort(reverse = True)
        h2 = l[0]*l[1]
        
    
    
    print(max(h1,h2))
    