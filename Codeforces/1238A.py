
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[0] - x[1] == 1:
        print('NO')
    else:
        print('YES')