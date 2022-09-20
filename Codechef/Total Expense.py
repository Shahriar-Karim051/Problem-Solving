# -*- coding: utf-8 -*-
"""
Created on Sun May 16 00:01:44 2021
Problem Code: FLOW009
@author: DELL
"""

for i in range(int(input())):
    q,p = map(int, input().split())
    expense = q*p
    print(expense*.9 if q>1000 else expense)