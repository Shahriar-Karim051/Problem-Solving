# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 08:17:41 2021
Problem Code: SNAKPROC
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    flag = 0
    cnt = 0
    for i in s:
        if i == 'H':
            cnt += 1
        elif i == 'T':
            cnt -= 1
        if cnt >1 or cnt <0:
            flag = 1
            break
    if cnt != 0:
        flag=1
    print('Valid' if flag == 0 else 'Invalid')
        