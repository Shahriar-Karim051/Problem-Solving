# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 02:50:40 2021
Problem Code: CLEANUP
@author: DELL
"""

for _ in range(int(input())):
    n,m = map(int,input().split())
    s = [int(s) for s in input().split()]
    job = []
    chef = []
    ass = []
    for i in range(1,n+1):
        if i not in s:
            job.append(i)
    for j in range(len(job)):
        if j % 2 != 0:
            ass.append(job[j])
        else:
            chef.append(job[j])
    print(*chef)
    print(*ass)