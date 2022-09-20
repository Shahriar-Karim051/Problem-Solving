# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:17:45 2021
Problem Code: CHN15A

@author: DELL
"""

for i in range(int(input())):
    n , k = map(int,input().split())
    a = [int(a) for a in input().split()]
    cnt = 0
    for j in a:
        if (j + k) % 7 == 0:
            cnt += 1
    print(cnt)