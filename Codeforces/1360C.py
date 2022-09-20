

for i in range(int(input())):
    a = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    ev = od = n = 0
    for j in range(a - 1):
        if x[j] % 2 == 0:
            ev += 1
        else:
            od += 1
        if x[j + 1] - x[j] == 1:
            n += 1
    if x[-1] % 2 == 0:
        ev += 1
    else:
        od += 1
    if ev % 2 == od % 2 == 0 or ev % 2 == od % 2 and n >= 1:
        print('YES')
    else:
        print('NO')
            
    