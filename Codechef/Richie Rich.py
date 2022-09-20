# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:17:58 2021
Problem Code: CHFRICH

@author: DELL
"""
import math
for _ in range(int(input())):
    a,b,x = map(int,input().split())
    print(math.ceil((b-a)/x))