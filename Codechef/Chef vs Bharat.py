# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 01:07:17 2021
Problem Code: CHEFORA
@author: DELL
"""
'''
def chefora(n):
    if n <= 9:
        return n
    else:
        b = n // 10
        b = list(str(b))
        b.reverse()
        return int(str(n)+"".join(b))
'''

def chefora(n):
    p = n
    n = n//10
    while n>0:
        p = p*10+n%10
        n = n//10
    return p

def power(a,b):
    mod = 10**9+7
    r = 1
    while b != 0:
        if b % 2 == 0:
            a = ((a%mod)**2)%mod
            b = b // 2
        else:
            r = ((r%mod)*(a%mod))%mod
            b -= 1
    return r

x = 10**5+1
a = [0]*(x)
asm = [0]*(x)
for i in range(1,x):
    a[i] = chefora(i)
    #print(a[i])
    asm[i] = a[i] + asm[i-1]
    #print(asm[i])
for _ in range(int(input())):
    l , r = map(int, input().split())
    print(power(a[l], (asm[r]-asm[l])))
    #print(asm[r]-asm[l])
    
        
    
    
    