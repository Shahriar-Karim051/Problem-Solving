# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:51:29 2021
Problem Code: POTATOES

@author: DELL
"""

def prime(x):
    flag = False
    for i in range(2,x):
        if x%i == 0:
            flag = True
            break
    return flag

for i in range(int(input())):
    x , y = map(int,input().split())
    j = 1
    while 1:
        z = prime(x+y+j)
        if z == False:
            print(j)
            break
        else:
            j+=1
        