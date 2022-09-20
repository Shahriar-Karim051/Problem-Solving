# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:47:46 2021
Problem Code: CANDY123

@author: DELL
"""

for _ in range(int(input())):
    l , b = map(int, input().split())
    flag = 0
    for i in range(1, l+b+1):
        if flag == 0:
            if l >= i:
                l -= i
                flag = 1
            else:
                print('Bob')
                break
        else:
            if b >= i:
                b -= i
                flag = 0
            else:
                print('Limak')
                break