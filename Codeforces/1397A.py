# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:45:19 2020

@author: DELL
"""
from collections import Counter
for _ in range(int(input())):
    c = int(input())
    s = ''
    for _ in range(c):
        n = input()
        s += n
    a = Counter(s)
    #print(a)
    cnt = 0
    for i in a:
        #b = a[i]
        #print(b)
        #print(type(b))
        if a[i] % c != 0:
            print('NO')
            cnt = 1
            break
    if cnt == 0:
        print('YES')
    