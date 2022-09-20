# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:07:26 2020

@author: DELL
"""

for _ in range(int(input())):
    n , k = map(int , input().split())
    a = [int(a) for a in input().split()]
    mid = n - ((n + 1) // 2) 
    ans = 0
    for i in range(k):
        ans += a[n * k - (i + 1)*(mid+1)]
    print(ans)