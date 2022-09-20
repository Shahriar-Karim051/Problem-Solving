# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:27:09 2021
TWTCLOSE
@author: DELL
"""
n,k = map(int, input().split())
cnt = 0
l = []
for i in range(k):
    a = input().split()
    if a[0] == 'CLOSEALL':
        cnt = 0
        l = []
    else:
        if a[1] not in l:
            cnt += 1
            l.append(a[1])
        else:
            cnt -= 1
            l.remove(a[1])
    print(cnt)