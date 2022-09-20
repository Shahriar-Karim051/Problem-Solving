# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 03:58:45 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a , b , c , d = (set(input().split()) for _ in range(4))
print(len(b - d))