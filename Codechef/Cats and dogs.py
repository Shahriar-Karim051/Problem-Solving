# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 01:10:11 2021
Problem Code: CATSDOGS
@author: DELL
"""

for _ in range(int(input())):
    c,d,l = map(int,input().split())
    a = 0
    if c > 2*d:
        a = c - (2*d)
    if l % 4 != 0:
        print('no')
    else:
        a = l // 4
        print('yes' if a >= d+a and a <=c+d  else 'no')