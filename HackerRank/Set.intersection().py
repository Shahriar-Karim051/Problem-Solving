# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 03:46:30 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set([int(b) for b in input().split()])
c = input()
d = set([int(d) for d in input().split()])
print(len(b & d))

'''
Enter your code here. Read input from STDIN. Print output to STDOUT
num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print(len(st1.intersection(st2)))
'''