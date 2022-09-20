
n = int(input())

x = [int(x) for x in input().split()]
x.sort()
if n % 2 == 0:
    print(x[n // 2 - 1])
else:
    print(x[n // 2])
