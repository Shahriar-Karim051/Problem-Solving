# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:58:45 2021
Problem Code: CHEFARRP

@author: DELL
"""



for i in range(int(input())):
    a = int(input())
    s = [int(s) for s in input().split()]
    cnt = 0
    for j in range(a):
        sm = 0
        mul = 1
        for k in range(j,a):
            sm += s[k]
            mul *= s[k]
            if sm == mul:
                cnt += 1
    print(cnt)
    