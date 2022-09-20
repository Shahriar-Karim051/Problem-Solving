# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:34:29 2021
Problem Code: MNMX

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    a.sort()
    print(a[0]*(n-1))