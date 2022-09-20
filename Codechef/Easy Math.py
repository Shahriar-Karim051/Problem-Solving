# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 23:03:16 2021
Problem Code: RPD
@author: DELL
"""

def sd(a):
    s = 0
    while a > 0:
        s += a % 10
        a = a // 10
    return s

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    mx = 0
    for i in range(n-1):
        for j in range(i+1,n):
            mx = max(mx,sd(a[i]*a[j]))
    print(mx)