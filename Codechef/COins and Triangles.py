# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:42:42 2021
Problem Code: TRICOIN

@author: DELL
"""

for i in range(int(input())):
    g = int(input())
    for n in range(g+2):
        if .5 * n * (n + 1) > g:
            print(n - 1)
            break
        