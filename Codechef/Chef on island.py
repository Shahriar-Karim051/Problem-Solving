# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 00:36:39 2021
Problem Code: CCISLAND

@author: DELL
"""

for _ in range(int(input())):
    x,y,xr,yr,d = map(int,input().split())
    if min((x/xr),(y/yr)) < d:
        print('NO')
    else:
        print('YES')