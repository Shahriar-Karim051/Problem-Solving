# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 19:01:16 2021

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    s = sum(a)
    k = 0
    if s%n != 0:
        print(-1)
    else:
        if n == 1 or len(set(a)) == 1:
            print(0)
        else:
            #print(a)
            for j in a:
                if j > s//n:
                    k += 1
            print(k)
    