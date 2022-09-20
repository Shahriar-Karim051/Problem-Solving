# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:23:18 2021

@author: DELL
"""

for _ in range(int(input())):
    x,y = map(int, input().split())
    a = list(input())
    r = a.count('R')
    l = a.count("L")
    u = a.count("U")
    d = a.count("D")
    flag = 0
    if x>0:
        if r < x:
            flag = 1
    else:
        if l < abs(x):
            flag = 1
    if y > 0:
        if u < y:
            flag = 1
    else:
        if d < abs(y):
            flag = 1
    print('YES' if flag == 0 else 'NO')