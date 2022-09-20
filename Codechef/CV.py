# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:54:08 2021
Problem Code: CV
@author: DELL
"""

vowel = ['a', 'e', 'i', 'o', 'u' ]
for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-1):
        if s[i] not in vowel and s[i+1] in vowel:
            cnt += 1
    print(cnt)