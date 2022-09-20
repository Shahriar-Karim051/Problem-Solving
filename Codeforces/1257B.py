

for i in range(int(input())):
    a , b = map(int , input().split())
    if a == 1 and b != 1:
        print('NO')
    elif a <= 3 and b > 3:
        print('NO')
    else:
        print('YES')