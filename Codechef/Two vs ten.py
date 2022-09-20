# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:18:46 2021
TWOVSTEN
@author: DELL
"""
for i in range(int(input())):
    n = input()
    if n[-1] == '0':
        print(0)
    elif n[-1] == '5':
        print(1)
    else:
        print(-1)
