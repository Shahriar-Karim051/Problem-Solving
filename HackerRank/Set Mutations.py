# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:24:11 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = set([int(i) for i in input().split()])
for _ in range(int(input())):
    c = input().split()
    d = set([int(d) for d in input().split()])
    eval('b.' + c[0] + '(d)' )
print(sum(b))