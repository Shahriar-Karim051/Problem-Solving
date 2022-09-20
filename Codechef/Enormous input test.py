# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:00:18 2021
Problem Code: INTEST

@author: DELL
"""

n , k = map(int , input().split())
cnt = 0
for i in range(n):
    if int(input()) % k == 0:
        cnt += 1
print(cnt)