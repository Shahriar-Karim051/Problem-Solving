# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:38:48 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()
index = 0

if re.search(k, s):
    while index+len(k) < len(s):
        m = re.search(k, s[index:])
        
        try:
            print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        except:
            break
        index += m.start() + 1 
else:
    print((-1, -1))
        
    
        
