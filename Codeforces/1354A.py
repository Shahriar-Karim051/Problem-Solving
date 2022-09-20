

for i in range(int(input())):
    a , b , c , d = map(int , input().split())
    if a <= b:
        print(b)
    else:
        if c <= d:
            print(-1)
        else:
            e = (a - b) // (c - d)
            if (a - b) % (c - d) != 0:
                e += 1
            print(b + c * e)