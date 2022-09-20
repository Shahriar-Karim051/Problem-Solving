# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:11:31 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    a = input()
    print(bool(re.match(r'^[+-]?[0-9]*[.][0-9]+$' , a)))