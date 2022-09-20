# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:28:49 2021
Problem Code: RECTANGL
@author: DELL
"""

for i in range(int(input())):
    l = [int(l) for l in input().split()]
    l.sort()
    print('YES' if l[0]==l[1] and l[2]==l[3] and l[0]!=[2] else 'NO')
        