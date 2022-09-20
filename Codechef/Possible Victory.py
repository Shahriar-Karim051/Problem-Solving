# -*- coding: utf-8 -*-
"""
Created on Fri May 14 23:39:01 2021
Problem Code: T20MCH

@author: DELL
"""

r , o , c = map(int , input().split())

print('yes' if (20-o)*36>(r-c) else 'no')