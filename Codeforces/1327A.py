# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:47:18 2020

@author: DELL
"""

for i in range(int(input())):
    n , k = map(int , input().split())
    if n < pow(k , 2):
        print('NO')
    elif n % 2 == 0 and k % 2 == 0:
        print('YES')
    elif n % 2 == 1 and k % 2 == 1:
        print('YES')
    else:
        print('NO')