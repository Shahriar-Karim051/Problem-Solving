
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    if x[-1] % 2 == 0:
        print(((x[-1] // 2) * x[0]) - (x[1] * (x[-1] // 2)))
    else:
        print((x[0] * (1 + (x[-1] // 2))) - (x[1] * (x[-1] // 2)))