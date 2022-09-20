
n , m = map(int , input().split())
cnt = 0


while n != m:
    if n >= m:
        cnt += n - m
        break
    if m % 2 == 0:
        m = m // 2
        cnt += 1
    else:
        m += 1
        cnt += 1
        m = m // 2
        cnt += 1
        
print(cnt)