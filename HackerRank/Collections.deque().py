# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 03:38:18 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    a = input().split() + ['']
    eval('d.' + a[0] + '(' + a[1] + ')')
    
print(*d)