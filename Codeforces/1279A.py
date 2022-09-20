
for i in range(int(input())):
    x = [int(x) for x in input().split()]
    x.sort()
    if x[0] + x[1] + 1 >= x[2]:
        print('YES')
    else:
        print('NO')