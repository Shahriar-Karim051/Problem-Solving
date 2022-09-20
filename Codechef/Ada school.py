# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:39:58 2021
Problem Code: ADASCOOL
@author: DELL
"""

for _ in range(int(input())):
    n,m = map(int,input().split())
    print('YES' if (n*m)%2 == 0 else 'NO')