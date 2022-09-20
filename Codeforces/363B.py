# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 02:17:17 2020

@author: DELL
"""

n , k = map(int , input().split())
a = [int(a) for a in input().split()]
ans = 1
s = sum(a[:k])
mn = s
#print(mn)
p = n + 1 - k

for i in range(1 , p):
    s = s - a[i - 1] + a[i + k - 1]
        #print(a[i - 1] , a[i + k - 1])
        #print(s)
    #print(s)
    
    if s < mn:
        #print(mn)
        mn = s
        ans = i + 1
    
print(ans)    

#print(l.index(min(l)) + 1)