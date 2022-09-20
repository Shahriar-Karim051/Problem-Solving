# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 07:24:37 2021
Problem Code: ATTND
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    d = {}
    l = []
    for i in range(n):
        a,b = input().split()
        l.append([a,b])
        d[a] = d.get(a,0)+1
    for j in l:
        print(' '.join(j) if d[j[0]]>1 else j[0])