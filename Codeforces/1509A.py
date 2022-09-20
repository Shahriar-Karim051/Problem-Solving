# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 03:26:23 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(*odd , end = " ")
    print(*even)