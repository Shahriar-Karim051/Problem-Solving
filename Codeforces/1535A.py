# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:43:06 2021

@author: DELL
"""

for _ in range(int(input())):
    s = [int(s) for s in input().split()]
    a = max(s[0],s[1])
    b = max(s[2],s[3])
    s.sort()
    if a in s[2:] and b in s[2:]:
        print('YES')
    else:
        print('NO')