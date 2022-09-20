# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:05:57 2021
Problem Code: MSNSADM1
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    mx = 0
    for i in range(n):
        s = 20*a[i] - 10*b[i]
        if s < 0:
            s = 0
        mx = max(mx,s)
    print(mx)
          
         

           