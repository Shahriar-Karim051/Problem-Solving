# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:22:44 2021
Problem Code: CSUB
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)
    c = s.count('1')
    print((c*(c+1)) // 2)