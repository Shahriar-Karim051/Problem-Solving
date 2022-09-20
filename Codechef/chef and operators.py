# -*- coding: utf-8 -*-
"""
Created on Sat May 15 00:13:01 2021
Problem Code: CHOPRT

@author: DELL
"""

for i in range(int(input())):
    a , b = map(int , input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')