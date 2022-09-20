# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:37:46 2021
Problem Code: ATM2

@author: DELL
"""

for i in range(int(input())):
    n , k = map(int, input().split())
    a = [int(a) for a in input().split()]
    l = []
    for j in a:
        if j <= k:
            l.append('1')
            k -= j
        else:
            l.append('0')
    print("".join(l))