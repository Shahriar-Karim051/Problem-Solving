# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:12:01 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set([int(b) for b in input().split()])
c = input()
d = set([int(d) for d in input().split()])
print(*sorted(b ^ d) , sep = '\n')


'''
a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')
'''