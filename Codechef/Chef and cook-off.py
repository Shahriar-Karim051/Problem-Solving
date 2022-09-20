# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:41:08 2021
Problem Code: CCOOK

@author: DELL
"""

l = ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean" ]

for _ in range(int(input())):
    a = [int(a) for a in input().split()]
    print(l[a.count(1)])