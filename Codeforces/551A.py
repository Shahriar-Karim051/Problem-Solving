

n = int(input())

x = [int(x) for x in input().split()]


for i in range(n):
    cnt = 1
    for j in range(n):
        if x[j] > x[i]:
            cnt += 1
    print(cnt , end = ' ')