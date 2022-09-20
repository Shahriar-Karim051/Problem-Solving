
for i in range(int(input())):
    a , b , c = map(int , input().split())
    cnt = 0
    if a >= 1:
        cnt += 1
        a -= 1
    if b >= 1:
        cnt += 1
        b -= 1
    if c >= 1:
        cnt += 1
        c -= 1
    a , b , c = sorted((a , b , c))
    if a >= 1 and c >= 1:
        cnt += 1
        a -= 1
        c -= 1
        
    if b >= 1 and c >= 1:
        cnt += 1
        b -= 1
        c -= 1
        
    if a >= 1 and b >= 1:
        cnt += 1
        a -= 1
        b -= 1
    
    if a >= 1 and b >= 1 and c >= 1:
        cnt += 1
    print(cnt)