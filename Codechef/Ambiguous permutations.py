# -*- coding: utf-8 -*-
"""
Created on Mon May 17 03:31:10 2021
Problem Code: PERMUT2

@author: DELL
"""
n = int(input())
while n != 0:
    l = [int(l) for l in input().split()]
    li = [0]*n
    for j in range(n):
        li[l[j]-1] = j+1
    print('ambiguous' if li == l else 'not ambiguous')
    n = int(input())