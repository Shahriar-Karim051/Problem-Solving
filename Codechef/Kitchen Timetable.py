# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:16:04 2021
KTTABLE
@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    cnt = 0
    if a[0] >= b[0]:
        cnt += 1
    for j in range(1,n):
        if a[j] - a[j-1] >= b[j]:
            cnt += 1
    print(cnt)