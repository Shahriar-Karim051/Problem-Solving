
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    y = [int(y) for y in input().split()]
    z = [int(z) for z in input().split()]
    if x[0] in y:
        print('YES')
    else:
        print('NO')