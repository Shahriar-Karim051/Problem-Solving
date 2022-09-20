# -*- coding: utf-8 -*-
"""
Created on Sat May 15 00:42:13 2021
Problem Code: BMI

@author: DELL
"""

for i in range(int(input())):
    m , h = map(int, input().split())
    bmi = m / (h * h)
    if bmi <= 18:
        print(1)
    elif bmi>18 and bmi<=24:
        print(2)
    elif bmi>24 and bmi<30:
        print(3)
    else:
        print(4)