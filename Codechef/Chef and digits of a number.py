# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:06:25 2021
Problem Code: LONGSEQ

@author: DELL
"""

for i in range(int(input())):
    n = input()
    one = n.count('1')
    if one == 1 or one == len(n)-1:
        print('Yes')
    else:
        print('No')