

n = int(input())

a = [int(a) for a in input().split()]
a.sort()
if n == 1:
    print(a[0] * a[0])
else:
    print(pow(sum(a[: n // 2]) , 2) + pow(sum(a[n // 2 :]) , 2))
