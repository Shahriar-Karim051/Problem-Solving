# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:43:21 2021
Problem Code: SIMDISH
@author: DELL
"""

for _ in range(int(input())):
    a = [str(a) for a in input().split()]
    b = [str(b) for b in input().split()]
    cnt = 0
    for i in b:
        if i in a:
            cnt +=1
    print('similar' if cnt >= 2 else 'dissimilar')