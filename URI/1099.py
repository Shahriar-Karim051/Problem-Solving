
n = int(input())

for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    cnt = 0
    for j in range(min(a,b) + 1 , max(a,b)):
        if j % 2 != 0:
            cnt = cnt + j
    print(cnt)
