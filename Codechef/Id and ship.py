# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:17:55 2021
Problem Code: FLOW010
@author: DELL
"""

for i in range(int(input())):
    n = input()
    n = n.lower()
    if n == 'b':
        print('BattleShip')
    elif n == 'c':
        print('Cruiser')
    elif n == 'd':
        print('Destroyer')
    else:
        print('Frigate')
    