# -*- coding: utf-8 -*-
"""
Created on Mon May 17 01:42:07 2021
Problem Code: LAPIN

@author: DELL
"""

for i in range(int(input())):
    s = input()
    if len(s) % 2 == 0:
        first = list(s[:len(s)//2])
        second = list(s[len(s)//2:])
    else:
        first = list(s[:len(s)//2])
        second = list(s[len(s)//2 + 1:])
    #print(first,second)
    
    first.sort()
    second.sort()
    if first == second:
        print('YES')
    else:
        print('NO')