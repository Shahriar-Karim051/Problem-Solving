

n , m = input().split()

n = int(n)
m = int(m)
a = m - n + 1
x = [int(x) for x in input().split()]

best = 1001

x.sort()

for i in range(a):
    if max(x[i : i + n]) - min(x[i : i + n]) < best:
        best = max(x[i : i + n]) - min(x[i : i + n])
    
print(best)