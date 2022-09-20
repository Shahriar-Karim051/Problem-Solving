# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:36:43 2020

@author: DELL
"""

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
