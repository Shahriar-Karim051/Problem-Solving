# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:50:25 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
a = set([int(a) for a in input().split()])
k = input()
b = set([int(b) for b in input().split()])
print(len(a | b))