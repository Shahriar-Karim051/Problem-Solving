

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    for j in range(n - 1):
        mx = max(a[j] , a[j + 1])
        mn = min(a[j] , a[j + 1])
        while mx / mn > 2:
            cnt += 1
            mn *= 2
    print(cnt)