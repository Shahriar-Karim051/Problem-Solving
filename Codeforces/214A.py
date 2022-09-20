

n , m = map(int , input().split())
cnt = 0

for i in range(min(n , m) + 1):
    for j in range(min(n,m) + 1):
        if (i * i) + j == n and (j * j) + i == m:
            cnt += 1
print(cnt)
        