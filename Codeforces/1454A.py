# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:45:11 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    print(n , end = ' ')
    for j in range(1 , n + 1):
        if j != n:
            print(j , end = ' ')
    print()