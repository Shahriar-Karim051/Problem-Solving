# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 08:42:58 2021
Problem Code: GOODBAD
@author: DELL
"""

for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(input())
    l=c=0
    chef = brother = 0
    for i in s:
        if i.islower():
            l += 1
        else:
            c += 1
    
    if l+k >= n:
        chef = 1
    if c+k >=n:
        brother = 1
    
    if chef == 1 and brother == 1:
        print('both')
    elif chef == 1:
        print('chef')
    elif brother == 1:
        print('brother')
    else:
        print('none')