# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:09:50 2020

@author: DELL
"""

for i in range(int(input())):
    a , b = map(int , input().split())
    ans = 2 * min(a , b) + 2 * (max(a , b) - min(a , b)) 
    print(ans - 1 if a !=b else ans)