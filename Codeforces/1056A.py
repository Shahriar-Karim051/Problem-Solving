
n = int(input())

x = [int(x) for x in input().split()]
c = set(x[1:])

for i in range(n - 1):
    y = [int(y) for y in input().split()]
    c = c.intersection(y[1:])
    
    
print(*c)