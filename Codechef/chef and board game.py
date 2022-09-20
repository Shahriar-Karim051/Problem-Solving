# -*- coding: utf-8 -*-
"""
Created on Sat May 15 01:00:13 2021
Problem Code: PCJ18B

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    s = 0
    for j in range(n//2 + 1):
        #print(j)
        s += pow((n - (2 *j)) , 2)
    print(s)