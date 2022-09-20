

x = [int(x) for x in input().split()]

x.sort()

if x[0] + x[1] > x[2] or x[1] + x[2] > x[3]:
    print('TRIANGLE')
elif x[0] + x[1] == x[2] or x[1] + x[2] == x[3]:
    print('SEGMENT')
else:
    print('IMPOSSIBLE')