
for i in range(int(input())):
    n , x = map(int , input().split())
    l = [int(l) for l in input().split()]
    even = odd = fl = 0
    for j in l:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        fl = 0
    elif even == 0:
        if x % 2 != 0:
            fl = 1
    else:
        for j in range(1 , odd + 1 , 2):
            if j + even >= x:
                fl = 1
                break
    if fl == 0:
        print('NO')
    else:
        print('YES')
        