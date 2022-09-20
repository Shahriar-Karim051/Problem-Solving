

for i in range(int(input())):
    n , d = map(int , input().split())
    x = [int(x) for x in input().split()]
    for j in range(1 , n):
        if x[j] != 0:
            if x[j] * j <= d:
                x[0] = x[0] + x[j]
                d = d - (x[j] * j)
            else:
                while d >= j and x[j] != 0:
                    x[0] = x[0] + 1
                    d = d - j
                    x[j] = x[j] - 1
    print(x[0])
            