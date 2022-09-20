

a = int(input())

x = [int(x) for x in input().split()]

x.sort()
s = 0

for i in range(a):
    s = s + abs((i + 1) - x[i])
    
print(s)