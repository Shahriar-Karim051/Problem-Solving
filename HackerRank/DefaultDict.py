# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 02:27:10 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n , m = map(int , input().split())
d = defaultdict(list)
for i in range(1 , n + 1):
    d[input()].append(i)
for j in range(m):
    a = input()
    if d[a]:
        print(*d[a])
    else:
        print(-1)
    

    
