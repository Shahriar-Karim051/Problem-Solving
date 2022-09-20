# -*- coding: utf-8 -*-
"""
Created on Mon May 17 03:12:09 2021
Problem Code: FLOW014

@author: DELL
"""

for i in range(int(input())):
    h,c,t = map(float, input().split())
    cnt = 0
    if h > 50:
        cnt+=1
    if c<0.7:
        cnt+=10
    if t > 5600:
        cnt += 100
        
    if cnt == 111:
        print(10)
    elif cnt == 11:
        print(9)
    elif cnt == 110:
        print(8)
    elif cnt == 101:
        print(7)
    elif cnt>0:
        print(6)
    else:
        print(5)

