# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:00:17 2021
Problem Code: PLAYPIAN
@author: DELL
"""

for _ in range(int(input())):
    s = list(input())
    flag = 0
    for i in range(0,len(s),2):
        if s[i] == s[i+1]:
            flag = 1
            break
    print('yes' if flag == 0 else 'no')