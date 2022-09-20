


for i in range(int(input())):
    x , y , n = map(int , input().split())
    rem = n // x
    while 1:
        if (rem * x) + y <= n:
            print(rem * x + y)
            break
        else:
            rem -= 1
        