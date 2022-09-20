# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:30:17 2021

@author: DELL
"""
#import math
for _ in range(int(input())):
    p , a , b , c = map(int , input().split())
    a1 = p // a
    if p % a != 0:
        a1 += 1
    b1 = p // b
    if p % b != 0:
        b1 += 1
    c1 = p // c
    if p % c != 0:
        c1 += 1
    
    #print(min(math.ceil(p / a) * a, math.ceil(p / b) * b, math.ceil(p / c) * c) - p)
    #print(math.ceil(p/a) )
    #print(1000000000000000000 / 999999999999999999)
    print(min(a1 * a, b1 * b, c1 * c) - p)