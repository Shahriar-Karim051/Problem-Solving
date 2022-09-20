# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:06:52 2021
Problem Code: CHEFSTUD
@author: DELL
"""

for _ in range(int(input())):
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == '<' and s[i+1] == '>':
            cnt += 1
    print(cnt)