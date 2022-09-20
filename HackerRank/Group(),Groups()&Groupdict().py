# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:31:00 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.search(r'([a-zA-Z0-9])\1+' , input())
print(m.group(1) if m else -1)