# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 00:14:16 2021
Problem Code: PLAYSTR
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    print('YES' if a.count('1') == b.count('1') else 'NO')