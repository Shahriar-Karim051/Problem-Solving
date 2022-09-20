# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 01:58:22 2021
Problem Code: LCH15JAB

@author: DELL
"""

from collections import Counter

for i in range(int(input())):
    s = input()
    a = Counter(s)
    flag = 0
    for j in a:
        if a[j] * 2 == len(s):
            flag = 1
            break
    print('YES' if flag == 1 else 'NO')