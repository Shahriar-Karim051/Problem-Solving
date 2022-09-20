# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:13:37 2021
Problem Code: RRJOKE
@author: DELL
"""


for _ in range(int(input())):
    n = int(input())
    for j in range(n):
        x,y = map(int,input().split())
    ans = 1
    for i in range(2,n+1):
        ans = ans ^ i
    print(ans)