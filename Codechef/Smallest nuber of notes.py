# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:18:16 2021
Problem Code: FLOW005
@author: DELL
"""

note = [100,50,10,5,2,1]
for i in range(int(input())):
    cnt = 0
    n = int(input())
    for j in note:
        cnt += n // j
        n = n % j
    print(cnt)