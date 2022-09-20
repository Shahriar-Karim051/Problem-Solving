

for i in range(int(input())):
    x = [int(x) for x in input().split()]
    d = 0
    for j in range(x[0] * (x[1] - x[2]) , (x[0] * (x[1] + x[2])) + 1):
        for k in range(x[3] - x[4] , x[3] + x[4] + 1):
            if j == k:
                d = 1
                break
    print('YES' if d == 1 else 'NO')