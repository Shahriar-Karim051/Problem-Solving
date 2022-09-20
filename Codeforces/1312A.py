
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[0] % x[1] == 0:
        print('YES')
    else:
        print('NO')