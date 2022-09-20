# -*- coding: utf-8 -*-
"""
Created on Mon May 17 03:49:11 2021
Problem Code: RECIPE

@author: DELL
"""

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

for i in range(int(input())):
    l = [int(l) for l in input().split()]
    li=[]
    if l[0] == 2:
        li = [x//gcd(l[1],l[2]) for x in l]
        print(*li[1:])
    else:
        
        a = l[1]
        for j in range(2,l[0]):
            a = gcd(a,l[j])
            li = [x//a for x in l]
        print(*li[1:])
        
    
    