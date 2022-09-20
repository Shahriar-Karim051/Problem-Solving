# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:03:18 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    i = 0
    j = 0
    k = -1
    l = []
    
    while i <= n // 2:
        l.append(a[j])
        l.append(a[k])
        i += 1
        j += 1
        k -= 1
    if n % 2 == 1:
        print(*l[:-1])
    else:
        print(*l[:-2])
        