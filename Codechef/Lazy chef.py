# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:57:00 2021
Problem Code: LAZYCHF

@author: DELL
"""

for _ in range(int(input())):
    x,m,d = map(int,input().split())
    print(min(m*x,x+d))