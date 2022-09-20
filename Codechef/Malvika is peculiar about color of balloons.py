# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:58:44 2021
Problem Code: CHN09

@author: DELL
"""

for i in range(int(input())):
    s = input()
    a = s.count('a')
    b = s.count('b')
    print(a if a<=b else b)