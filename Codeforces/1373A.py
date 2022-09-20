
for i in range(int(input())):
    a , b , c = map(int , input().split())
    if a < c:
        d = 1
    else:
        d = -1
    if a * b > c:
        e = b
    else:
        e = -1
    print(d , e)