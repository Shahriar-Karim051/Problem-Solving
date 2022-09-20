# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:49:22 2021
Problem Code: COCONUT

@author: DELL
"""
import math
for _ in range(int(input())):
    a,b,A,B = map(int,input().split())
    print(math.ceil(A/a)+math.ceil(B/b))