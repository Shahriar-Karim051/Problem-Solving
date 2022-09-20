# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:05:41 2021
Problem Code: CIELRCPT

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    s = n // 2048
    a = n % 2048
    a = list(bin(a))
    print(s + a.count('1'))