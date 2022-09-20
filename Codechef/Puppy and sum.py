# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:26:14 2021
Problem Code: PPSUM

@author: DELL
"""

for i in range(int(input())):
    d , n = map(int, input().split())
    for j in range(d):
        s = (n * (n + 1))//2
        n = s
    print(s)