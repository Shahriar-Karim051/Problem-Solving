

for i in range(int(input())):
    a , b , c = map(int , input().split())
    d = max(a , b)
    b = min(a , b)
    cnt = e = 0
    
    while d <= c:
        b = b + d
        e = d
        d = b
        b = e
        cnt += 1
    print(cnt)
        