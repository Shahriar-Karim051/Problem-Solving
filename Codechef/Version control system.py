# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:00:37 2021
Problem Code: VCS

@author: DELL
"""

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    cnt0=cnt1=0
    for i in range(1,n+1):
        if i in a and i in b:
            cnt0 += 1
        elif i not in a and i not in b:
            cnt1 += 1
    print(cnt0,cnt1)