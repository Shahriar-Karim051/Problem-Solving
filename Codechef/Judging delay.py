# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:57:48 2021
Problem Code: JDELAY
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n):
        s,j = map(int,input().split())
        if j - s > 5:
            cnt += 1
    print(cnt)