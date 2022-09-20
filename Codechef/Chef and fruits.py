# -*- coding: utf-8 -*-
"""
Created on Tue May 18 01:10:11 2021
Problem Code: FRUITS

@author: DELL
"""

for i in range(int(input())):
    n,m,k = map(int,input().split())
    if abs(n-m) >= k:
        print(abs(n-m) - k)
    else:
        print(0)