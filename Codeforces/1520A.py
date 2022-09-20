# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:11:25 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = list(input())
    d = 0
    for i in range(n-1):
        if a[i] != a[i + 1]:
            if a[i] in a[i+1:]:
                d = 1
                break
    print('NO' if d == 1 else 'YES')