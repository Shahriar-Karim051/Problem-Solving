

for i in range(int(input())):
    a , b = map(int , input().split())
    c = b // (a - 1)
    d = b % (a - 1)
    if a == b:
        print(a + 1)
    elif d == 0:
        print(c * a - 1)
    else:
        print(c * a + d)
    