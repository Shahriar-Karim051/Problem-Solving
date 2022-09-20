
n = int(input())

x = [int(x) for x in input().split()]
x.sort()

print(x[-1] - x[0] - n + 1)