# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 02:55:20 2020

@author: DELL
"""

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    a = input().split() + ['']
    #cmd = a[0]
    #cmd += '(' + a[1] + ')'
    eval('s.' + a[0] + '(' + a[1] + ')' )
print(sum(s))


