# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:22:20 2021
Problem Code: SEGM01
@author: DELL
"""

for _ in range(int(input())):
    s = list(input())
    l = []
    flag = 0
    for i in range(len(s)):
        if s[i] == '1':
            l.append(i)
    for j in range(len(l)-1):
        if l[j+1] - l[j] != 1:
            flag = 1
            break
    if len(l) == 0:
        print('NO')
    else:
        print('YES' if flag == 0 else 'NO')
            
        