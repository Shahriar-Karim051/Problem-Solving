l = []
ans = 0
n = int(input())
for i in range(n):
    p = int(input())
    l.append(p - 1)
    

    
for j in range(n):
    cnt = 0
    x = l[j]
    while x != -2:
        x = l[x]
        cnt += 1
    ans = max(ans , cnt)
    
print(ans + 1)