# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 07:31:08 2021
Problem Code: SIMPSTAT
@author: DELL
"""

for _ in range(int(input())):
    n,k= map(int,input().split())
    a = [int(a) for a in input().split()]
    s = sum(a)
    a.sort()
    for i in range(k):
        s -= a[i]
    for j in range(1,k+1):
        s -= a[-j]
    print(s/(n - (2*k)))