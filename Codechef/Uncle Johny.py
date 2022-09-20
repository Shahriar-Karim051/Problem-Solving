# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 02:42:16 2021
Problem Code: JOHNY
@author: DELL
"""

for _ in range(int(input())):
    a = int(input())
    n = [int(n) for n in input().split()]
    k = int(input())
    cnt = 0
    for i in n:
        if i <= n[k-1]:
            cnt += 1
    print(cnt)