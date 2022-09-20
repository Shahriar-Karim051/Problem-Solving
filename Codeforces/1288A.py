import math

for i in range(int(input())):
    n , d = map(int , input().split())
    c = 0
    if d <= n:
        print('YES')
    else:
        m = int(math.sqrt(d)) + 10
        for j in range(m):
            if j + (d  / (j + 1) )<= n:
                c = 1
                break
        if c == 1:
            print('YES')
        else:
            print('NO')
        