# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:25:49 2021

@author: DELL
Problem Code: SAVWATER

"""

for i in range(int(input())):
    h,x,y,c = map(int , input().split())
    if h * (x + y // 2) <= c:
        print('yes')
    else:
        print('no')