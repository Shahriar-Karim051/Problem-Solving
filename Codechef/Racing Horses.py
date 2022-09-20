# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 01:50:18 2021
Problem Code: HORSES
@author: DELL
"""

for _ in range(int(input())):
    a = int(input())
    n = [int(n) for n in input().split()]
    n.sort(reverse = True)
    mn = 1000000000
    for i in range(a-1):
        mn = min(n[i]-n[i+1], mn)
        #print(mn)
    print(mn)
        
        