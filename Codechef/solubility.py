# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:16:32 2021

@author: DELL
code: SOLBLTY
"""

for i in range(int(input())):
    x ,a,b = map(int, input().split())
    print(((100-x)*b+a)*10)