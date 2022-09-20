
n = int(input())

for i in range(n):
    a = int(input())
    cnt = 0
    while a != 1:
        if a % 2 == 0:
            a = a // 2
            cnt = cnt + 1
        elif a % 3 == 0:
            a = (a // 3) * 2
            cnt = cnt + 1
        elif a % 5 == 0:
            a = (a // 5) * 4
            cnt = cnt + 1
        else:
            cnt = -1
            break
        
    if cnt == -1:
        print(-1)
    else:
        print(cnt)
    
            