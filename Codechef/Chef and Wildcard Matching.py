# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:40:17 2021
Problem Code: TWOSTR

@author: DELL
"""

for i in range(int(input())):
    x = input()
    y = input()
    flag = 0
    for j in range(len(x)):
        if x[j] != '?' and y[j] != '?' and x[j] != y[j]:
            flag = 1
            break
    print('Yes' if flag == 0 else 'No')
            