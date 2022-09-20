# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:57:45 2021

@author: DELL
Problem Code: DIV03

"""

for i in range(int(input())):
    a = [int(a) for a in input().split()]
    k = int(input())
    if sum(a) <= k:
        print(1)
    else:
        for j in range(1,11):
            if a[-j] <= k:
                k -= a[-j]
                #print(j , k)
            else:
                print(11-j)
                break
                #print(j)