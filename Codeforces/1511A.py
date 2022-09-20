# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:36:02 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    print(a.count(1)+a.count(3))