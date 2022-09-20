

x = [int(x) for x in input().split()]

y = [int(y) for y in input().split()]


if sum(x) > sum(y):
    print('NO')
elif x[0] > y[0]:
    print('NO')
elif y[0] + y[1] - x[0] < x[1]:
    print('NO')
elif sum(y) - x[0] - x[1] < x[2]:
    print('NO')
else:
    print('YES')
