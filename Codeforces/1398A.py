# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:21:07 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    #a.sort()
    if a[0] + a[1] <= a[-1]:
        print(1 , 2 , n)
    else:
        print(-1)