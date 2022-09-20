# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:23:32 2021
Problem Code: STRPALIN

@author: DELL
"""

for _ in range(int(input())):
    a = input()
    b = input()
    flag = 0
    for i in a:
        if i in b:
            flag = 1
            break
    print('No' if flag == 0 else 'Yes')