# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:15:29 2021
Problem Code: FRGTNLNG

@author: DELL
"""



for _ in range(int(input())):
    n , k = map(int, input().split())
    a = input().split()
    d = dict()
    for i in a:
        d[i] = 'NO'
    for j in range(k):
        b = input().split()
        for z in range(1, len(b)):
            if b[z] in a:
                d[b[z]] = 'YES'
    for y in d:
        print(d[y] , end = ' ')
    
    