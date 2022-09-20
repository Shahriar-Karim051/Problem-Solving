# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:06:13 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    mn = min(a)
    for i in a:
        if i > mn:
            cnt += 1
    print(cnt)