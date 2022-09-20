# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:35:40 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
a = input()
b = [int(b) for b in input().split()]
c = Counter(b)
d = c.most_common()[-1]
print(d[0])