# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:58:57 2020

@author: DELL
"""
'''
import roman

try:
    print(0 < roman.fromRoman(input()) < 4000)
except:
    print(False)
'''


thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"






import re
print(str(bool(re.match(regex_pattern, input()))))