# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:34:56 2020

@author: DELL
"""

for i in range(int(input())):
    n , c0 , c1 , h = map(int , input().split())
    s = input()
    z = s.count('0')
    o = s.count('1')
    print(min((c0*z + c1*o) , (c0*n + o*h) , (z*h + c1*n)))