# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 02:07:27 2020

@author: DELL
"""

def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)