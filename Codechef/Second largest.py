# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:15:17 2021
Problem Code: FLOW017

@author: DELL
"""

for i in range(int(input())):
    l = [int(l) for l in input().split()]
    l.sort()
    print(l[1])