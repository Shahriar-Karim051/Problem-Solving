

for i in range(int(input())):
    n , k = map(int , input().split())
    a = [int(a) for a in input().split()]
    a.sort()
    b = [int(b) for b in input().split()]
    b.sort(reverse = True)
    if a[0] > b[0]:
        print(sum(a))
    else:
        for j in range(k):
            if a[j] <= b[j]:
                a[j] = b[j]
            else:
                break
        print(sum(a))
    