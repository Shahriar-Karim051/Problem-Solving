# -*- coding: utf-8 -*-
"""
Created on Tue May 18 00:14:42 2021
Problem Code: COMM3

@author: DELL
"""
import math
for i in range(int(input())):
    r = int(input())
    x0,y0 = map(int,input().split())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    cnt=0
    x0x1= math.sqrt((x1-x0)**2 + (y1-y0)**2)
    x1x2= math.sqrt((x2-x1)**2 + (y2-y1)**2)
    x0x2= math.sqrt((x2-x0)**2 + (y2-y0)**2)
    #print(x0x1,x1x2,x0x2)
    if x0x1 <= r:
        cnt += 1
    
        
    if x1x2 <= r:
        cnt += 1
    
    if x0x2 <= r:
        cnt += 1
   
    print('yes' if cnt >= 2 else 'no')