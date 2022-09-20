# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:03:05 2021
Problem Code: COPS

@author: DELL
"""

for i in range(int(input())):
    m , x , y = map(int, input().split())
    a = [int(a) for a in input().split()]
    l = []
    for j in a:
        for m in range(x*y + 1):
            l.append(j-m)
            l.append(j+m)
    cnt = 0
    for k in range(1,101):
        if k not in l:
            cnt += 1
    print(cnt)
        