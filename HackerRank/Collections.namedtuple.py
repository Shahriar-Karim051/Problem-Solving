# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:55:52 2020

@author: DELL
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())
score = namedtuple('score' , input().split())
marks = [score(*input().split()).MARKS for i in range(n)]
print("%.2f" %(sum(map(int , marks)) / n))

'''
n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))
'''