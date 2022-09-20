# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:46:41 2021
Problem Code: TTENIS
@author: DELL
"""

for _ in range(int(input())):
    s = list(input())
    win = 0
    lose = 0
    for i in s:
        if i == '1':
            win += 1
        else:
            lose += 1
    print('WIN' if win > lose else 'LOSE')
        