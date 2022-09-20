n = int(input())
for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    r = cnt = 0
    while a > 0:
        if a % b == 0:
            a = a // b
            cnt = cnt + 1
        else:
            r = a % b
            cnt = cnt + r
            a = a - r
    print(cnt)