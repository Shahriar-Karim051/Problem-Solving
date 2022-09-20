# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:00:53 2021

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    for j in a:
        if j % 2 != 0:
            cnt += 1
    print('Yes' if cnt == n else 'No')