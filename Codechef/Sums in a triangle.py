# -*- coding: utf-8 -*-
"""
Created on Mon May 17 02:07:59 2021
Problem Code: SUMTRIAN

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    li = []
    for i in range(n):
        l = [int(l) for l in input().split()]
        li.append(l)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            li[i][j] = li[i][j]+max(li[i+1][j],li[i+1][j+1])
    print(li[0][0])
        
    