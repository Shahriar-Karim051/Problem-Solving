# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:19:59 2021
Problem Code: FLOW013
@author: DELL
"""

for i in range(int(input())):
    l = [int(l) for l in input().split()]
    print('YES' if sum(l) == 180 else 'NO')