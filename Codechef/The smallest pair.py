# -*- coding: utf-8 -*-
"""
Created on Mon May 17 02:40:47 2021
Problem Code: SMPAIR

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    l = [int(l) for l in input().split()]
    l.sort()
    print(l[0]+l[1])