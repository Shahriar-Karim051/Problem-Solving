# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:55:36 2021
Problem Code: RECTSQ

@author: DELL
"""
import math
for _ in range(int(input())):
    n , m = map(int, input().split())
    c = math.gcd(n,m)
    print((n//c)*(m//c))