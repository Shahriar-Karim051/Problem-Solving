# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 03:12:57 2020

@author: DELL
"""


from itertools import permutations
a = '1234'
n = list(permutations(a))
ans = 10000000
for _ in range(int(input())):
    p11 , p12 = map(int , input().split())
    p21 , p22 = map(int , input().split())
    p31 , p32 = map(int , input().split())
    p41 , p42 = map(int , input().split())
    cur = 0
    l1 = [0]*4
    l2 = [0]*4
    for i in n:
        cnt = 0
        for j in i:
            #print(j)
            if j == '1':
                l1[cnt] = p11
                l2[cnt] = p12
                    
            elif j == '2':
                l1[cnt] = p21
                l2[cnt] = p22
                    
            elif j == '3':
                l1[cnt] = p31
                l2[cnt] = p32
                    
            else:
                l1[cnt] = p41
                l2[cnt] = p42
            cnt += 1
            if cnt == 4:
                break
                
            
        #print(l1)
        cur += abs(l1[0] - l1[3]) + abs(l1[2] - l1[1])+abs(l2[0] - l2[1])+abs(l2[2] -l2[3])
        #print(cur)
        xseg0 = max(min(l1[0] , l1[3]) - max(l1[1] , l1[2]) , min(l1[1] ,l1[2]) - max(l1[0] , l1[3]))
        xseg1 = max(- min(l1[0] , l1[3]) + max(l1[1] , l1[2]) , -min(l1[1] ,l1[2]) + max(l1[0] , l1[3]))
        yseg0 = max(min(l2[0] , l2[1]) - max(l2[3] , l2[2]) , min(l2[2] ,l2[3]) - max(l2[1] , l2[0])) 
        yseg1 = max(- min(l2[0] , l2[1]) + max(l2[3] , l2[2]), -min(l2[2] ,l2[3]) + max(l2[1] , l2[0]))
        c = -min(xseg1 , yseg1) + max(xseg0 , yseg0)
        #print(c)
        cur += 2 * max(0 , c)
        ans = min(ans , cur)
        #print(ans)
    print(ans)
              