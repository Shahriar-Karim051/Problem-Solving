
n = input()

x = [int(x) for x in input().split()]

x.sort()

max = x[-1]

a = len(x) * max - sum(x)

print(a)