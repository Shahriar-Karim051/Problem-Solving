# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:08:55 2021
Problem Code: AREAPERI

@author: DELL
"""

l = int(input())
b = int(input())

area = l * b
peri = 2 * ( l + b)

if area > peri:
    print('Area')
    print(area)
elif area < peri:
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(area)