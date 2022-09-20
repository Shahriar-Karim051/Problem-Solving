

n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if abs(x[0] - x[1]) % (x[2] + x[3]) == 0:
        print(abs(x[0] - x[1]) // (x[2] + x[3]))
    else:
        print(-1)