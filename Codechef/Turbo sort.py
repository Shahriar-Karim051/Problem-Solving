# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:27:49 2021
Problem Code: TSORT

@author: DELL
"""
l = []
for i in range(int(input())):
    l.append(int(input()))
    
l.sort()
for j in l:
    print(j)