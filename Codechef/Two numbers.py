# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:53:56 2021
Problem Code: TWONMS

@author: DELL
"""

for _ in range(int(input())):
    a,b,n = map(int,input().split())
    if n % 2 == 1:
        a *= 2
    print(max(a,b)//min(a,b))