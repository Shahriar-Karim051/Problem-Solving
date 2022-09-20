# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:11:34 2021
Problem Code: MATCHES

@author: DELL
"""

matches = [6,2,5,5,4,5,6,3,7,6]

for _ in range(int(input())):
    a,b = map(int,input().split())
    s = str(a+b)
    cnt = 0
    for i in s:
        cnt += matches[int(i)]
    print(cnt)
    
    