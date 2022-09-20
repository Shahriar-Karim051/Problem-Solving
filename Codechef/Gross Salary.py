# -*- coding: utf-8 -*-
"""
Created on Mon May 17 02:35:00 2021
Problem Code: FLOW011

@author: DELL
"""

for i in range(int(input())):
    salary = int(input())
    if salary < 1500:
        print(salary*2)
    else:
        print(salary*1.98+500)