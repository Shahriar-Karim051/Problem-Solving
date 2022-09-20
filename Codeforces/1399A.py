

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    cnt = 0
    if n == 1:
        print('YES')
    else:
        a.sort()
        for j in range(len(a) - 1):
            if a[j + 1] - a[j] <= 1:
                cnt += 1
        print('YES' if n - cnt == 1 else 'NO')
            