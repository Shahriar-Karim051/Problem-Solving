# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:57:27 2021
Problem Code: CLIPLX

@author: DELL
"""

for _ in range(int(input())):
    x,y = map(int,input().split())
    cnt = 0
    while x > y:
        x -= 2
        y -= 1
        cnt += 1
    print(cnt)