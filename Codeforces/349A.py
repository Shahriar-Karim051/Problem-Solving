

a = b = 0

n = int(input())

x = [int(x) for x in input().split()]


if x[0] == 50 or x[0] == 100:
    print('NO')
    exit()

for i in x:
    if i == 25:
        a = a + 1
    elif i == 50:
        if a < 1:
            print('NO')
            exit()
        else:
            a = a - 1
            b = b + 1
    elif i == 100:
        if a > 0 and b > 0:
            a = a - 1
            b = b - 1
        
        elif a >= 3:
            a = a - 3
        else:
            print('NO')
            exit()
    
print('YES')