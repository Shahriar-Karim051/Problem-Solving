# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:20:56 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    if n <= 3:
        print(n -1)
    elif n % 2 == 0:
        print(2)
    else:
        print(3)