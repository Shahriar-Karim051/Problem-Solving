# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 04:57:16 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(input().split())
n = int(input())
print(all([a.issuperset(set(input().split())) for _ in range(n)]))

'''
a = set(input().split())
counter , n = 0, int(input())
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)
'''