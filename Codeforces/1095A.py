# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:54:19 2021

@author: DELL
"""

n = int(input())
a = input()

i = 1
while 1:
    s = (i*(i+1))//2
    if s <= n:
        print(a[s-1], end = '')
        i += 1
    else:
        break
    
    