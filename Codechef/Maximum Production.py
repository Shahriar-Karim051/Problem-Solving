# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:22:03 2021
Problem Code: EITA

@author: DELL
"""

for i in range(int(input())):
    d,x,y,z = map(int, input().split())
    print(max((7*x),((d*y)+((7-d)*z))))