# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 19:30:56 2021
Problem Code: PRGIFT
@author: DELL
"""

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = [int(a) for a in input().split()]
    cnt = 0
    for i in a:
        if i % 2 == 0:
            cnt += 1
    if k == 0 and cnt == n:
        print('NO')
    else:
        if cnt >= k:
            print('YES')
        else:
            print('NO')