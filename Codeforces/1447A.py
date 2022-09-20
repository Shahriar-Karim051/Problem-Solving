# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:10:47 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    print(n)
    print(*[i for i in range(1 , n + 1)])