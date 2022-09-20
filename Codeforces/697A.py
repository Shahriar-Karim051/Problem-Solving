

t , s , x = map(int , input().split())
r = 0
while t <= x:
    if t == x:
        r = 1
        break
    else:
        t += s
    if t + 1 == x:
        r = 1
        break
    
print('NO' if r == 0 else 'YES')
    
    