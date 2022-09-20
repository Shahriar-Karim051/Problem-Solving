# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 07:06:28 2021
Problem Code: TICKETS5
@author: DELL
"""

for _ in range(int(input())):
    s = input()
    cnt = 0
    if s[0]!=s[1]:
        x = s[0]
        y = s[1]
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == x:
                cnt += 1
        else:
            if s[i] == y:
                cnt += 1
        
    print('YES' if cnt==len(s) else 'NO')