# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:13:24 2020

@author: DELL
"""

def print_rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    #print(items)
    items = items[:-1]+items[::-1]
    #print(items)
    for i in items:
        temp = data[-(i+1):]
        #print(temp)
        row = temp[::-1]+temp[1:]
        #print(temp[::-1] , temp[1:])
        #print(row)
        print("-".join(row).center(n*4-3, "-"))


n = int(input())
print_rangoli(n)
