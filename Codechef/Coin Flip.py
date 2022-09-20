# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 03:09:30 2021
Problem Code: CONFLIP
@author: DELL
"""

for _ in range(int(input())):
    for g in range(int(input())):
        i,n,q = map(int,input().split())
        if i == 1:
            tail = (n+1)//2
            head = n-tail
        else:
            head = (n+1)//2
            tail = n-head
        print(head if q == 1 else tail)
    
    