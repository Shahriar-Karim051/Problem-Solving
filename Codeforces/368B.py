# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 02:12:15 2020

@author: DELL
"""

n , m = map(int , input().split())
a = [int(a) for a in input().split()]

#s = [i for i in range(1 , n + 1)]
#s = [0] * (n + 1)
d = []
#ans = 0
'''
for i in a:
    if i not in d:
        ans += 1
        s.append(ans)
        d.append(i)
    else:
        s.append(ans)

s.reverse()
print(s)
'''
'''
for _ in range(m):
    l = int(input())
    #print(s.index(l))
    print(len(set(a[s.index(l):])))

'''
#j = n 
'''
for j in range(n - 1, -1, -1):
    #j -= 1
    if a[j] not in d:
        s[j] = s[j + 1] + 1
        d.append(a[j])
    else:
        s[j] = s[j + 1]
for i in range(m):
    l = int(input())
    print(s[l - 1])
'''

for j in range(n):
    #j -= 1
    d.append(len(set(a[j:])))
for i in range(m):
    l = int(input())
    print(d[l - 1])    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    