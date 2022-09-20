# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:51:31 2021
Problem Code: XXOORR

@author: DELL
"""
import math
for i in range(int(input())):
    n,x = map(int,input().split())
    l = [0]*33
    a = [int(a) for a in input().split()]
    for j in a:
        s = str('{:033b}'.format(j))
        
        for k in range(len(s)):
            if s[k] == '1':
                l[k] += 1
    cnt = 0
    #print(l)
    for m in l:
        cnt += math.ceil(m/x)
        #print(m , math.ceil(m/k))
    print(cnt)