# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:45:00 2021
Problem Code: CO92JUDG
@author: DELL
"""

for _ in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(b) for b in input().split()]
    alice = sum(a)-max(a)
    bob = sum(b)-max(b)
    if alice < bob:
        print('Alice')
    elif alice > bob:
        print('Bob')
    else:
        print('Draw')