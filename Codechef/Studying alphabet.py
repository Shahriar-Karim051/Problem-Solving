# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:25:41 2021
Problem Code: ALPHABET

@author: DELL
"""

s = set(list(input()))

for i in range(int(input())):
    a = set(list(input()))
    print('Yes' if a.issubset(s) == True else 'No')