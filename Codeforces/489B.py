

b = int(input())
x = [int(x) for x in input().split()]
x.sort()
g = int(input())
y = [int(y) for y in input().split()]
y.sort()
cnt = 0
for i in range(b):
    for j in range(g):
        if abs(x[i] - y[j]) <= 1:
            y[j] = 1000
            cnt += 1
            break
            
print(cnt)