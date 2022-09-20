# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:49:44 2021
Problem Code: REMISS

@author: DELL
"""

for i in range(int(input())):
    a , b = map(int, input().split())
    print(max(a,b) , a+b)