# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 07:41:48 2021
Problem Code: LOSTMAX
@author: DELL
"""

for _ in range(int(input())):
    a = [int(a) for a in input().split()]
    a.sort(reverse = True)
    if a[0] != len(a)-1:
        print(a[0])
    else:
        print(a[1])
    