# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:40:49 2020

@author: DELL
"""

for i in range(int(input())):
    m , n = map(int , input().split())
    c = 0
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    for i in b:
        if i in a:
            print('YES')
            print(1 , i)
            c = 1
            break
    if c == 0:
        print('NO')

    