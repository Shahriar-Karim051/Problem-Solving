# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 03:32:29 2021
Problem Code: DWNLD
@author: DELL
"""

for _ in range(int(input())):
    n,k = map(int,input().split())
    cnt = 0
    for i in range(n):
        t,d = map(int,input().split())
        if k >= t:
            k = k - t
        else:
            cnt += (t-k)*d
            k = 0
    print(cnt)