
a = int(input())
x = [int(x) for x in input().split()]

y = sorted(set(x))
print(y[-2])