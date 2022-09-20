
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    y = [int(y) for y in input().split()]
    if (x[0] + x[1] == 0 or y[2] < y[4]) and (x[2] + x[3] == 0 or y[3] < y[5]):
        if y[2] <= y[0] - x[0] + x[1] and y[0] - x[0] + x[1] <= y[4] and y[1] + x[3] - x[2] >= y[3] and y[1] + x[3] - x[2] <= y[5]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')