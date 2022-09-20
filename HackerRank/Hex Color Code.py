# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:40:46 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
import re
for i in range(int(input())):
    a = input()
    m = re.findall(r'(#(?:[\da-f]{3}){1 , 2})(?!\w)(?=.*;)' , a , re.IGNORECASE)
    for j in m:
        print(j)
'''
import re
for i in range(int(input())):
    matches = re.findall(r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE)
    for m in matches:
        print(m)