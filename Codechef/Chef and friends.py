# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 19:15:39 2021
Problem Code: FRK
@author: DELL
"""
l = ['ch','he','ef']
cnt = 0
for _ in range(int(input())):
    s = input()
    for i in range(len(s)-1):
        p = s[i]+s[i+1]
        if p in l:
            cnt += 1
            break
print(cnt)