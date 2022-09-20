# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:15:20 2021
Problem Code: ICL1902

@author: DELL
"""
import math
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n != 0:
        s = math.floor(math.sqrt(n))
        n -= s*s
        #print(n)
        cnt += 1
    print(cnt)