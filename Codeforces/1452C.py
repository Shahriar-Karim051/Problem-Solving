# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 12:25:38 2020

@author: DELL
"""

for _ in range(int(input())):
    s = input()
    tlb = slb = cnt = 0
    for i in s:
        if i == '(':
            slb += 1
        elif i == '[':
            tlb += 1
        elif i == ')':
            if slb > 0:
                cnt += 1
                slb -= 1
        else:
            if tlb > 0:
                cnt += 1
                tlb -= 1
    print(cnt)
                
    
    