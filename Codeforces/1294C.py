
n = int(input())


for k in range(n):
    z = int(input())
    l = []
    for i in range(2 , z):
        if z % i == 0:
            l.append(i)
            z = z // i
            break
        if (i * i) > z:
            break
    for j in range(2 , z):
        if z % j == 0 and j not in l:
            l.append(j)
            z = z // j
            break
        if (j * j) > z:
            break
    if len(l) < 2 or z == 1 or z in l:
        print('NO')
    else:
        print('YES')
        print(l[0] , l[1] , z)
        
    