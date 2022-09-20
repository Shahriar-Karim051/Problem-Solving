# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:52:34 2021
Problem Code: CYCLICQD

@author: DELL
"""

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a+c == 180:
        print('YES')
    else:
        print('NO')