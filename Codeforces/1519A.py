# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:49:16 2021

@author: DELL
"""

for _ in range(int(input())):
    r,b,d = map(int, input().split())
    print('YES' if min(r,b)*(d+1) >= max(r,b) else 'NO')
    