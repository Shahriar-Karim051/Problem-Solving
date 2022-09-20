# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:41:17 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    ans = 'True'
    try:
        re.compile(input())
    except re.error:
        ans = 'False'
    print(ans)