# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 03:27:17 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    try:
        a , b = map(int , input().split())
        print(a // b)
    except BaseException as e:
        print('Error Code:' , e)