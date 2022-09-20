# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:20:08 2021
Problem Code: ELEVSTRS
@author: DELL
"""

for i in range(int(input())):
    n,v1,v2 = map(int,input().split())
    if (2*n)/v2 <= ((2**.5)*n)/v1:
        print('Elevator')
    else:
        print('Stairs')