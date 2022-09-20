# -*- coding: utf-8 -*-
"""
Created on Tue May 18 01:40:06 2021
Problem Code: CHEFSTLT

@author: DELL
"""

for i in range(int(input())):
    s1 = input()
    s2 = input()
    q = d = 0
    for j in range(len(s1)):
        if s1[j] == '?' or s2[j] == '?':
            q += 1
        elif s1[j] != s2[j]:
            d += 1
    print(d , d+q)
        