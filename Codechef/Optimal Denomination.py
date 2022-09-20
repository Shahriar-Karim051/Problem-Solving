# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:51:24 2021
Problem Code: MINNOTES

@author: DELL
"""

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a , a)


for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    if n == 1:
        print(1)
    else:
        b = sum(a)
        s = float('Inf')
        l = []
        fwd = [0]*n
        fwd[0] = a[0]
        bwd = [0]*n
        bwd[n-1] = a[-1]
        #print(bwd)
        
        for j in range(1,n):
            fwd[j] = gcd(fwd[j-1],a[j])
        for k in range(n-2,-1,-1):
            bwd[k]=gcd(bwd[k+1],a[k])
        l.append(bwd[1])
        for m in range(1,n-1):
            l.append(gcd(fwd[m-1],bwd[m+1]))
        l.append(fwd[n-2])
        #print(fwd)
        #print(bwd)
        #print(l)
            
        for z in range(n):
            s = min(s, ((b-a[z])//l[z])+1)
        
    
        
        print(s)