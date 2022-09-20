# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:39:31 2021

@author: DELL

"""
import math
def ps(a):
    r = math.sqrt(a)
    if int(r+0.5)**2 == a:
        return 1
    else:
        return 0
    
    

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    for i in a:
        if ps(i) == 1:
            cnt += 1
    print('YES' if cnt != n else 'NO')
    
    
