# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:43:57 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print('3 1 2')
    elif n%2 == 1:
        print('3 1 2' , end = ' ')
        for i in range(4,n+1):
            if i%2 == 0:
                print(i+1, end = ' ')
            else:
                print(i-1, end = ' ')
    else:
        for i in range(1,n+1):
            if i % 2 == 0:
                print(i-1, end = ' ')
            else:
                print(i + 1, end = ' ')
    