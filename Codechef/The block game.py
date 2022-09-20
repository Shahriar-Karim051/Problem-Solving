# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:28:38 2021
Problem Code: PALL01

@author: DELL
"""

for i in range(int(input())):
    n = input()
    p = list(n)
    p.reverse()
    print('wins' if int(n) == int("".join(p)) else 'loses')