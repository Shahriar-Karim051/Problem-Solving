# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:50:52 2020

@author: DELL
"""

string, substring = (input().strip(), input().strip())
s = 0
for i in range(len(string) - len(substring) + 1):
    if string[i : i + len(substring)] == substring:
        s += 1
print(s)
#print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))