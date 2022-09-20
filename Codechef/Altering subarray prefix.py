# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:37:09 2021
Problem Code: ALTARAY

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 1
    l = []
    l.append(1)
    for i in range(n-1,0,-1):
        if a[i]*a[i-1] < 0:
            cnt += 1
            l.append(cnt)
        else:
            cnt = 1
            l.append(cnt)
    l.reverse()
    print(*l)
            