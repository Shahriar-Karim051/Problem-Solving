# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:47:47 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    a , b = [set(input().split()) for _ in range(4)] [1 : : 2]
    print(a.issubset(b))