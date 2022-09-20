# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:30:05 2021

@author: DELL
"""

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    s = Counter(a)
    for d in s:
        if s[d] == 1:
            print(a.index(d)+1)