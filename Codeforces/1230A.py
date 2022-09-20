

x = [int(x) for x in input().split()]

if x[0] + x[1] == x[2] + x[3]:
    print('YES')
elif x[0] + x[2] == x[1] + x[3]:
    print('YES')
elif x[0] + x[3] == x[2] + x[1]:
    print('YES')
elif x[0] == x[1] + x[2] + x[3]:
    print('YES')
elif x[1] == x[0] + x[2] + x[3]:
    print('YES')
elif x[2] == x[0] + x[1] + x[3]:
    print('YES')
elif x[3] == x[0] + x[1] + x[2]:
    print('YES')
else:
    print('NO')