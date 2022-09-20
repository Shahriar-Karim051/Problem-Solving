# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:35:50 2020

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    r = list(input())
    b = list(input())
    blue = 0
    red = 0
    for j in range(n):
        if int(r[j]) > int(b[j]):
            red += 1
        elif int(b[j]) > int(r[j]):
            blue += 1
    if red == blue:
        print('EQUAL')
    elif red > blue:
        print('RED')
    else:
        print('BLUE')