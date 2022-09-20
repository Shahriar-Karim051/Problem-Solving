# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:21:52 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    s = sum(a)
    if s == n:
        print(0)
    elif s<=n:
        print(1)
    else:
        print(s-n)