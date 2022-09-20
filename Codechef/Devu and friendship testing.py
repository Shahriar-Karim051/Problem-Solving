# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:43:44 2021
Problem Code: CFRTEST

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    print(len(set(a)))