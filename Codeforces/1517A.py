# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:07:36 2021

@author: DELL
"""

def sd(a):
    s=0
    if a <= 9:
        return a
    else:
        while a>0:
            s += a%10
            a = a//10
        return s

for _ in range(int(input())):
    n = int(input())
    if n % 2050 != 0:
        print(-1)
    else:
        a = n // 2050
        print(sd(a))
        
        