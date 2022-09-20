# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:40:39 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    for i in range(n+1):
        if 2 ** i > n:
            print(2**(i-1) - 1)
            break