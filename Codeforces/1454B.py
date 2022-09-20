# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:19:58 2020

@author: DELL
"""
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = [int(l) for l in input().split()]
    a = Counter(l)
    ans = 1000000
    #print(a)
    for i in a:
        if a[i] == 1:
            ans = min(ans , i)
    print(l.index(ans) + 1 if ans != 1000000 else -1)