# -*- coding: utf-8 -*-
"""
Created on Fri May 14 23:48:16 2021
Problem Code: SNCKYEAR

@author: DELL
"""

l = [2010, 2015, 2016, 2017, 2019]
for i in range(int(input())):
    print('HOSTED' if int(input()) in l else 'NOT HOSTED')