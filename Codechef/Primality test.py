# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:58:12 2021
Problem Code: PRB01
@author: DELL
"""
import math
for i in range(int(input())):
    n = int(input())
    a = 0
    if n == 1:
        print('no')
    else:
        for j in range(2 , math.floor(math.sqrt(n))+1):
            if n % j == 0:
                a = 1
                break
        print('yes' if a== 0 else 'no')