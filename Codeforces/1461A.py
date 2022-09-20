# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:25:26 2020

@author: DELL
"""
a = ['a' , 'b' , 'c']
for i in range(int(input())):
    n , k = map(int , input().split())
    print('a' * (k - 1) , end ='' )
    for j in range(n - k + 1):
        print(a[j % 3] , end = '')
    print()
    