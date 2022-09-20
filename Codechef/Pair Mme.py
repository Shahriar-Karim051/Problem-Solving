# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:32:16 2021

@author: DELL
Problem Code: SUMPOS

"""

for i in range(int(input())):
    x , y , z = map(int , input().split())
    if x + y == z or y + z == x or x + z == y:
        print('YES')
    else:
        print('NO')
    