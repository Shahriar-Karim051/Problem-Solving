# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:07:28 2020

@author: DELL
"""

for i in range(int(input())):
    s = int(input())
    if  s > 45:
        print(-1)
    elif s <= 9:
        print(s)
    else:
        l = []
        i = 9
        while 1:
            s -= i
            l.append(str(i))
            i -= 1
            if s == 0:
                break
            elif s < i:
                l.append(str(s))
                break
        
            
        l.sort()
        #print(l)
        print(''.join(l))
    
        