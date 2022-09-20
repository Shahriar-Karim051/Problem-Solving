# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:45:32 2021
Problem Code: MOVIEWKN

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    l = [int(l) for l in input().split()]
    r = [int(r) for r in input().split()]
    mx = rating = 0
    index = 999999999999
    for i in range(n-1,-1,-1):
        if l[i]*r[i] >= mx and r[i] >= rating:
            mx = l[i]*r[i]
            index = min(i+1,index)
            rating = r[i]
            
            
    print(index)
            
    