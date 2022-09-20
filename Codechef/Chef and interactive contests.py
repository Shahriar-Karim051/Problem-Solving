# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:39:31 2021
Problem Code: CHFINTRO
@author: DELL
"""

n,r = map(int, input().split())
for _ in range(n):
    print('Bad boi' if int(input())<r else 'Good boi')