# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:29:24 2021
Problem Code: TLG

@author: DELL
"""
mx1 = mx2 = 0
n = int(input())
p1 , p2 = map(int, input().split())
if p1 > p2:
   mx1 = max(mx1 , p1-p2)
else:
   mx2 = max(mx2 , p2-p1)
for i in range(n-1):
    a,b = map(int , input().split())
    p1 +=a
    p2 +=b
    if p1 > p2:
        mx1 = max(mx1 , p1-p2)
    else:
        mx2 = max(mx2 , p2-p1)
        
if mx1>mx2:
    print(1,mx1)
else:
    print(2,mx2)