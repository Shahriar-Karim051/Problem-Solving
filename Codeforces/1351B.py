

for i in range(int(input())):
    x = [int(x) for x in input().split()]
    x.sort()
    a , b = input().split()
    a = int(a) 
    b = int(b)
    if a == x[-1]:
        if x[0] + b == a:
            print('YES')
        else:
            print('NO')
    elif b == x[-1]:
        if x[0] + a == b:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')