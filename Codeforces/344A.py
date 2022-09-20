

n = int(input())
cnt = 1
l = []
for _ in range(n):
    a = int(input())
    l.append(a)


for i in range(n - 1):
    if l[i] != l[i + 1]:
        cnt += 1
        
        
print(cnt)
    