
n , m = map(int , input().split())
cnt = 0
for i in range(n):
    x = [int(x) for x in input().split()]
    for j in range(0 , len(x) - 1 , 2):
        if x[j] + x[j + 1] > 0:
            cnt += 1
print(cnt)