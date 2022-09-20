# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:28:51 2021

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    mx = a.index(max(a))
    mn = a.index(min(a))
    print(min(max(mx,mn)+1, n-min(mx,mn), n-max(mx,mn)+min(mx,mn)+1, n-min(mx,mn)+max(mx,mn)+1))
    