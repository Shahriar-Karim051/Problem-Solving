
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if 2 * x[1] <= x[2]:
        print(x[0] * x[1])
    else:
        print(((x[0] - (x[0] % 2)) // 2) * x[2] + (x[0] % 2) * x[1])