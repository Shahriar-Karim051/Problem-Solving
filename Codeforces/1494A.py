# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:03:49 2021

@author: DELL
"""

for _ in range(int(input())):
    s = input()
    f = s.count(s[0])
    l = s.count(s[-1])
    cnt = 0
    p = len(s) // 2
    if s[-1] == s[0]:
        print('no')
    else:
        rs = {'A','B','C'} ^ (set(s[0]).union(set(s[-1])))
        
        r = s.count(*rs)
        d=0
        if f < p:
            if f + r != p:
                print('no')
            else:
                for i in s:
                    if i == s[-1]:
                        cnt -= 1
                    else:
                        cnt += 1
                    #print(cnt)
                    if cnt < 0:
                        d = 1
                print('yes' if d == 0 else 'no')
        elif l < p:
            if l + r != p:
                print('no')
            else:
                for i in s:
                    if i == s[0]:
                        cnt += 1
                    else:
                        cnt -= 1
                    if cnt < 0:
                        d = 1
                print('yes' if d == 0 else 'no')
        else:
            for i in s:
                if i == s[0]:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt < 0:
                    d = 1
            print('yes' if d == 0 else 'no')
            
                
                
        
        
    
    
    