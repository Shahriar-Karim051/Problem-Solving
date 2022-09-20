# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:07:50 2021
Problem Code: CHEFSQ

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    m = int(input())
    b = [int(b) for b in input().split()]
    x = -1
    cnt = 0
    for i in b:
        if i in a and a.index(i)>x:
            cnt += 1
            x = a.index(i)
    print('Yes' if cnt==m else 'No')