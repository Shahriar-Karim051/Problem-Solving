

a , b = map(int , input().split())

n = a // 2 + a % 2

if a < b:
    print(-1)
else:
    if n % b == 0:
        print(n)
    else:
        m = n + (b - (n % b))
        print(m)