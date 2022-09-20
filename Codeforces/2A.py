

from collections import Counter

n = int(input())

x = [input() for j in range(n)]

a = Counter()

l = []

for i in range(n):
    name , point = x[i].split()
    a[name] += int(point)
    l.append((name , a[name]))

mx = max(a.values())

print([name for (name , point) in l if point >= mx and a[name] == mx][0])

