
x = [int(x) for x in input().split()]

if min(x[0] , x[1] , x[2]) == x[0]:
    y = x[0]
    b = x[0] + 1
    r = x[0] + 2
    while b > x[1] or r > x[2]:
        y = y - 1
        b = b - 1
        r = r - 1
elif min(x[0] , x[1] , x[2]) == x[1]:
    y = x[1] - 1
    b = x[1] 
    r = x[1] + 1
    while b > x[1] or r > x[2]:
        y = y - 1
        b = b - 1
        r = r - 1
else:
    y = x[2] - 2
    b = x[2] - 1
    r = x[2] 
    while b > x[1] or r > x[2]:
        y = y - 1
        b = b - 1
        r = r - 1
        
print(y + b + r)
        
    