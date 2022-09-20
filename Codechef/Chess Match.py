# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:28:50 2021
Problem Code: BLITZ3_2

@author: DELL
"""

for _ in range(int(input())):
    n , a , b = map(int, input().split())
    print(2*(180+n) - (a+b))