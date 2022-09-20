# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:07:42 2021
Problem Code: MISSP

@author: DELL
"""

for i in range(int(input())):
    a = []
    b = []
    for j in range(int(input())):
        n = int(input())
        if n not in a:
            a.append(n)
        else:
            b.append(n)
    if set(a) != set(b):
        print(*(set(a) - set(b)))
    else:
        print(0)
        
    
            
'''            
for _ in range(int(input())):
    n=int(input()) 
    u=0
    for i in range(n):
        g=int(input()) 
        u=u^g
        #print(u)
    print(u)
'''