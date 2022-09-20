
m , s = map(int , input().split())

if s == 0 and m > 1:
        print(-1 , -1)
        exit()
t = s
mx = [0] * m
mn = [0] * m
i = 0
j = -1
mini = ''
maxi = ''
while 1:
    if s == 0:
        break
    elif s >= 9:
        mx[i] = 9
        i += 1
        s = s - 9
    else:
        mx[i] = s
        break
    if i >= m and s != 0:
        print(-1 , -1)
        exit()
        

if t == 0:
   mn[0] = 0
else:
   mn[0] = 1
   t -= 1
   
while 1:
    if t >= 9:
        mn[j] = 9
        j -= 1
        t -= 9
    else:
        if mn[j] == 1:
            mn[j] = t + 1
        else:
            mn[j] = t 
        break
        
for i in mn:
    mini += str(i)
    
for j in mx:
    maxi += str(j)
    
print(mini , maxi)
  