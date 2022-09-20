# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:53:09 2021

@author: DELL
"""

for _ in range(int(input())):
    n,d = map(int,input().split())
    a = [int(a) for a in input().split()]
    a.sort()
    if a[-1] <= d:
        print('YES')
    elif a[0]+a[1] <= d:
        print('YES')
    else:
        print('NO')