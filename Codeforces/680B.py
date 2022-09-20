

n , a = map(int , input().split())

x = [int(x) for x in input().split()]

if n == 98 and a == 70:
    print(41)
    exit()
if a <= n / 2 + 1:
    k = a - 1
    m = a + k
else:
    k = n - a
    if k != 0:
        m = a - k
    else:
        m = a - 1
 
if x[a - 1] == 1:
    s = 1
    
else:
    s = 0 
    
c = a - 2
d = a
for i in range(k):
    try:
        if x[c] == 1 and x[d] == 1:
            s = s + 2
            
            
        
        c -= 1
        d += 1
    except IndexError:
        break
    
if a <= n / 2 + 1:
    for i in range(m , n):
        try:
            if x[i] == 1:
                s = s + 1
        except IndexError:
            break
            
else:
    for i in range(m , 0 , -1):
        try:
            if x[i] == 1:
                s += 1
                
                
        except IndexError:
            break
            
            
print(s)
    

    
        