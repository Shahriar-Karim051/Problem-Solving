# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:11:49 2021
Problem Code: RAINBOWA

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    s = set(a)
    #print(s)
    l = {1,2,3,4,5,6,7}
    if a == a[::-1] and s == l:
        print('yes')
    else:
        print('no')