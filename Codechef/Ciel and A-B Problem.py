# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:31:43 2021
Problem Code: CIELAB
@author: DELL
"""

a,b = map(int,input().split())
d = a-b

if (d+1) % 10 == 0:
    print(d-1)
else:
    print(d+1)