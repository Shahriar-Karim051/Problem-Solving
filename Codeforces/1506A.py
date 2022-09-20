# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:32:20 2021

@author: DELL
"""

for i in range(int(input())):
    n,m,x = map(int,input().split())
    x = x - 1
    r = x % n
    c = x//n
    print((r*m)+c+1)