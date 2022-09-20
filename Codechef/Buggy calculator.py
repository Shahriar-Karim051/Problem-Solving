# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 20:33:39 2021
Problem Code: BUGCAL
@author: DELL
"""

for _ in range(int(input())):
    a,b = input().split()
    l = max(len(a),len(b))
    a,b = a.rjust(l,'0'), b.rjust(l,'0')
    s = ''
    for j in range(l):
        c = (int(a[j])+int(b[j]))%10
        s += str(c)
    print(int(s))