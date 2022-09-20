# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:09:27 2021
Problem Code: CNOTE
@author: DELL
"""

for _ in range(int(input())):
    x,y,k,n = map(int,input().split())
    flag = 0
    page = x - y
    for i in range(n):
        p,c = map(int,input().split())
        if page <= p and k >= c:
            flag = 1
    print("LuckyChef" if flag == 1 else "UnluckyChef")
        