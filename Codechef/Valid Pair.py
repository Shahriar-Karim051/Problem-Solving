# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:45:41 2021

@author: DELL
code: SOCKS1
"""

a , b , c = map(int , input().split())
if a==b or b==c or c==a:
    print('YES')
else:
    print('NO')