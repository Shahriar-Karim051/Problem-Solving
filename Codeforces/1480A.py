# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 03:17:55 2021

@author: DELL
"""

for _ in range(int(input())):
    a = input()
    s = ""
    for i in range(len(a)):
        if i % 2 == 0:
            if a[i] == 'a':
                s += 'b'
            else:
                s += 'a'
        else:
            if a[i] == 'z':
                s += 'y'
            else:
                s += 'z'
    print(s)