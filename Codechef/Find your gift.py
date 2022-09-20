# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:30:15 2021
Problem Code: GIFTSRC

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    cntx = cnty = 0
    flag = -1
    for i in s:
        if i == 'L':
            if flag != 0:
                cntx -= 1
                flag = 0
        if i == 'R':
            if flag != 0:
                cntx += 1
                flag = 0
        if i == 'U':
            if flag != 1:
                cnty += 1
                flag = 1
        elif i == 'D':
            if flag != 1:
                cnty -= 1
                flag = 1
    print(cntx,cnty)
        