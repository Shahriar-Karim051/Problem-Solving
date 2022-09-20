# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:35:00 2021
Problem Code: FLOW016

@author: DELL
"""

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a , a)
    
def lcm(a,b):
    return (a // gcd(a,b)) * b

for i in range(int(input())):
    a , b = map(int, input().split())
    print(gcd(a,b) , lcm(a,b))
    