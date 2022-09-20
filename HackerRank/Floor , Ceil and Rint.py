# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:03:04 2020

@author: DELL
"""

import numpy
numpy.set_printoptions(legacy='1.13')

a = numpy.array(input().split() , float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))



