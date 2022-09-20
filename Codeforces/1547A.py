# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:15:03 2021

@author: DELL
"""

for i in range(int(input())):
    a = input()
    xa,ya = map(int, input().split())
    xb,yb = map(int,input().split())
    xf,yf = map(int,input().split())
    d = abs(xa-xb)+abs(ya-yb)
    if xa==xf and xb==xf:
        if min(ya,yb) <= yf and max(ya,yb) >= yf:
            d += 2
    elif ya==yf and yb==yf:
        if min(xa,xb) <= xf and max(xa,xb) >= xf:
            d += 2
    print(d)