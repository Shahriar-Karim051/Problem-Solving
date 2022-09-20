# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:41:52 2021
Problem Code: HEADBOB

@author: DELL
"""

for i in range(int(input())):
    n = int(input())
    a = input()
    I=NI=0
    for j in a:
        if j=='Y':
            NI+=1
        elif j=='I':
            I+=1
    if I>0 and NI == 0:
        print('INDIAN')
    elif NI>0 and I==0:
        print('NOT INDIAN')
    else:
        print('NOT SURE')