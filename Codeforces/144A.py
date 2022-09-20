from more_itertools import locate
z = input()

x = [int(x) for x in input().split()]


k = len(x) - 1

a = list(locate(x, lambda y1: y1 == max(x)))

b = list(locate(x, lambda y2: y2 == min(x)))

print(a)
print(b)
c = len(a) -1
print(c)

d = len(b) - 1
print(d)

print(a[c] - b[d] + k)
