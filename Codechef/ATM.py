# -*- coding: utf-8 -*-
"""
Created on Sat May 15 01:24:48 2021
Problem Code: HS08TEST

@author: DELL
"""

x , y = map(float, input().split())

if x % 5 != 0 or x > (y - 0.5):
    print('%.2f'%y)
else:
    print('%.2f'%(y - x-.5))