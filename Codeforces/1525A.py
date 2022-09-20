# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:23:58 2021

@author: DELL
"""

import math
for _ in range(int(input())):
    k=int(input())
    print(100//math.gcd(k,100-k))