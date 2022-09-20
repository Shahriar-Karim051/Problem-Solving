# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:09:13 2021
Problem Code: FCTRL
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    s = 0
    while 1:
        n = n // 5
        s += n
        if n < 5:
            break
    print(s)