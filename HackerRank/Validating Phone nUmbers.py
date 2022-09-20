# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:40:47 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    if re.match(r'[789]\d{9}$' , input()):
        print('YES')
    else:
        print('NO')