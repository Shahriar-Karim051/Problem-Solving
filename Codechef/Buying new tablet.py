# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:07:56 2021
Problem Code: TABLET

@author: DELL
"""

for i in range(int(input())):
    n,b = map(int,input().split())
    area = 0
    for j in range(n):
        w,h,p=map(int,input().split())
        if p<=b:
            area = max(area,w*h)
    print(area if area != 0 else 'no tablet')