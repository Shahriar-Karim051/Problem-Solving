# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:57:30 2020

@author: DELL
"""

for i in range(int(input())):
    a = input().split()
    n = set([int(n) for n in input().split()])
    m = set([int(m) for m in input().split()])
    print(len(n & m))