# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:44:44 2021

@author: DELL
"""
import math
for _ in range(int(input())):
    n , k = map(int, input().split())
    l=[]
    for i in range(math.ceil(k / 2), k):
        l.append(i)
    for j in range(k + 1 , n + 1):
        l.append(j)
    print(len(l))
    print(*l)
    