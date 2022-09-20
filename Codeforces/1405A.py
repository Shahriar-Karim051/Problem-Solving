# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:10:52 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    print(*a[::-1])
    