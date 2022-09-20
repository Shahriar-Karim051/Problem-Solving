

n = int(input())



for i in range(n):
    z = int(input())
    x = y = c = 0
    for j in range(z):
        a , b = input().split()
        a = int(a)
        b = int(b)
        if a < x or b < y or b - y > a - x:
            c = c + 1
        x = a
        y = b
    if c > 0:
        print('NO')
    else:
        print('YES')
        
    