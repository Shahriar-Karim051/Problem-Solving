# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:28:15 2020

@author: DELL
"""

import numpy

n , m = map(int,input().split())
l = []
for _ in range(n):
    l.append([int(i) for i in input().split()])
print(numpy.prod(numpy.sum(l , axis = 0)))
    

'''
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0)))
'''