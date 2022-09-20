
n = int(input())

x = [int(x) for x in input().split()]
x.sort()
s = 0

if n == 2:
    print(abs(x[0] - x[1]))
    exit()
else:
    for i in range(0, n, 2):
        s = s + abs(x[i] - x[i + 1])
    
print(s)