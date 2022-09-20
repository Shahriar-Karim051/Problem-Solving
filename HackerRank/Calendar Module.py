# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 03:10:54 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month , day , year = map(int , input().split())
print(calendar.day_name[calendar.weekday(year , month , day)].upper())