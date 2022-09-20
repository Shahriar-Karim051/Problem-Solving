# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:03:36 2020

@author: DELL
"""
def sn(x):
    if x >= 0:
        return 1
    else:
        return -1
for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    s = 0
    i = -1
    while i < n - 1:
        i = i + 1
        mx = a[i]
        #print(i)
        j = i
        while j < n and sn(a[i]) == sn(a[j]):
            mx = max(mx , a[j])
            j += 1
        s = s + mx
        i = j - 1
    
    print(s)