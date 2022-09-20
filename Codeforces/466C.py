# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:53:47 2020

@author: DELL
"""

n = int(input())
a = [int(a) for a in input().split()]
s = sum(a)
if s % 3 != 0:
    print(0)
else:
    s = s // 3
    t = 0
    ct = 0
    res = 0
    for i in range(n - 1):
        t += a[i]
        if t == 2 * s:
            res += ct
        if t == s:
            ct += 1
    print(res)