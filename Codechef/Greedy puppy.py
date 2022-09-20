# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:55:03 2021
Problem Code: GDOG

@author: DELL
"""

for i in range(int(input())):
    n,k = map(int,input().split())
    mx=0
    for j in range(1,k+1):
        mx = max(mx,n%j)
    print(mx)