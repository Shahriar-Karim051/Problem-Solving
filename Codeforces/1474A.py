# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:05:30 2021

@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    b = input()
    ans = 1
    print(1 , end = '')
    for i in range(1,n):
        if 1 + int(b[i])!= ans + int(b[i-1]):
            ans = 1
            print(1 , end ='')
        else:
            ans = 0
            print(0, end = '')
    print()
    
        
        
    
        
        