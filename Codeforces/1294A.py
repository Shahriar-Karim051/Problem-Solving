

n = int(input())
b = []

for i in range(n):
    a = [int(a) for a in input().split()]
    
    m = max(a[0], a[1], a[2])
    if ((a[-1] - ((3 * m) - a[0] - a[1] - a[2]))) % 3 == 0 and (a[-1] - ((3 * m) - a[0] - a[1] - a[2])) >= 0:
        print("YES")
    else:
        print("NO")