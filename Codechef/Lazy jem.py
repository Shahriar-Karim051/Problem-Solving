# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:46:17 2021
Problem Code: TALAZY

@author: DELL
"""

for _ in range(int(input())):
    n,b,m = map(int,input().split())
    s = 0
    while n > 1:
        if n % 2 == 0:
            a = n // 2
        else:
            a = (n+1) // 2
        s += (a*m)+b
        n -= a
        m *= 2
    print(s+m)