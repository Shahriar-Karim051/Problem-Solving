# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:12:03 2021
Problem Code: AMR15A

@author: DELL
"""

lucky = not_lucky = 0

n = int(input())
s = [int(i) for i in input().split()]

for i in s:
    if i % 2== 0:
        lucky += 1
    else:
        not_lucky += 1
print('READY FOR BATTLE' if lucky>not_lucky else 'NOT READY')