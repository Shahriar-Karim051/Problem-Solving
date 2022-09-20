
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[3] % x[2] <= x[1] and x[0] * x[2] + x[1] >= x[3]:
        print('YES')
    else:
        print('NO')