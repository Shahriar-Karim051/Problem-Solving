
na , nb = map(int , input().split())
k , m = map(int , input().split())

a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]
b.sort(reverse = True)

if a[k - 1] < b[m - 1]:
    print('YES')
else:
    print('NO')

