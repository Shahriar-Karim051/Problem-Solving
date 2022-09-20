# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:49:27 2020

@author: DELL
"""

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    #return(numpy.array(arr[::-1] , float))
    return numpy.flipud(numpy.array(arr , float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)