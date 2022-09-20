# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:26:16 2020

@author: DELL
"""

import numpy

a , b = map(int , input().split())
l = []
for i in range(a):
    c = [int(c) for c in input().split()]
    l.append(c)
  
#l = [list(map(int , input().split()) ) for _ in range(a)]
print(numpy.max(numpy.min(l , axis = 1)))


