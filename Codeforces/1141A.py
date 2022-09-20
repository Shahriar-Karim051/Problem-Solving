

a , b = input().split()

a = int(a)
b = int(b)
c = 0
if b % a != 0:
    print(-1)
else:
    d = b // a
    while d % 2 == 0:
        d = d // 2
        c = c + 1
    while d % 3 == 0:
        d = d // 3
        c = c + 1
    if d != 1:
        print(-1)
    else:
        print(c)
        
    
    