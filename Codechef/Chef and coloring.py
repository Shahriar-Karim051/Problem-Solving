# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:15:31 2021
Problem Code: COLOR

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = list(input())
    r = a.count('R')
    g = a.count('G')
    b = a.count('B')
    print(n - max((r,g,b)))