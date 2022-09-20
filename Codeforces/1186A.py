
x = [int(x) for x in input().split()]

if min(x[1] , x[2]) >= x[0]:
    print("YES")
else:
    print("NO")