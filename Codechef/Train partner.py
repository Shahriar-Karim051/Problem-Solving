# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 07:49:08 2021
Problem Code: ANKTRAIN
@author: DELL
"""

l = ['SL','LB','MB','UB','LB','MB','UB','SU']

for _ in range(int(input())):
    n = int(input())
    a = n%8
    if a==0:
        print(str(n-1)+l[a])
    elif a <= 3:
        print(str(n+3)+l[a])
    elif a>= 4 and a<=6:
        print(str(n-3)+l[a])
    else:
        print(str(n+1)+l[a])
    