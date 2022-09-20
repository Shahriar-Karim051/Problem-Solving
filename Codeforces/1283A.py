
n = int(input())

for i in range(n):
    x = [int(x) for x in input().split()]
    print(1440 - ((60 * x[0]) + x[1]))