

for i in range(int(input())):
    n = int(input())
    a = [int(a) for a in input().split()]
    mna = min(a)
    b = [int(b) for b in input().split()]
    mnb = min(b)
    cnt = 0
    for j in range(n):
        cnt += max(abs(mna - a[j]) , abs(mnb - b[j]))
    print(cnt)