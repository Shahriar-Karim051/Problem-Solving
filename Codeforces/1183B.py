
for i in range(int(input())):
    n , k = map(int , input().split())
    a = [int(a) for a in input().split()]
    a.sort()
    if a[-1] - a[0] - k <= k:
        print(a[0] + k)
    else:
        print(-1)