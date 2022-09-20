from math import factorial as fact

b = int(input())


a = [int(a) for a in input().split()]
a.sort()

s = 0

for i in range(b):
    c = b + i
    s += abs(a[i] - a[c])
 
x = fact(2 * b) // fact(b) // fact(b)

print((s * x) % 998244353)