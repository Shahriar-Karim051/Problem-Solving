# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:54:34 2020

@author: DELL
"""

for _ in range(int(input())):
    n , q = map(int , input().split())
    s = input()
    for _ in range(q):
        l , r = map(int , input().split())
        c = 'NO'
        for i in range(l - 1):
            if s[i] == s[l - 1]:
                c = 'YES'
        for j in range(r , n):
            if s[j] == s[r - 1]:
                c = 'YES'
        print(c)