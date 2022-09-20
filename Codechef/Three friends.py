# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:53:39 2021
Problem Code: THREEFR
@author: DELL
"""

for _ in range(int(input())):
    x,y,z = map(int,input().split())
    x,y,z = sorted((x,y,z))
    print('yes' if z - y - x == 0 else 'no')