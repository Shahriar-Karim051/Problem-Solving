# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:17:18 2021
Problem Code: WATSCORE
@author: DELL
"""

for _ in range(int(input())):
    l = [0]*8
    for i in range(int(input())):
        p,s = map(int,input().split())
        if p <= 8:
            l[p-1] = max(l[p-1],s)
    print(sum(l))
    