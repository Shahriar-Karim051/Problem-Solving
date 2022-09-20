# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 00:01:38 2021

@author: DELL
"""
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    c = Counter(a)
    mx = 1
    for i in c:
        mx = max(mx,c[i])
    print(mx)