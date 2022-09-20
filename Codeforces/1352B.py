
for i in range(int(input())):
    n , k = map(int , input().split())
    if n - 2 * (k - 1) > 0 and (n - 2 * (k - 1)) % 2 == 0:
        print('YES')
        print(n - 2 * (k - 1) , str('2 ') * (k - 1))
    elif n - (k - 1) > 0 and (n - (k - 1)) % 2 != 0:
        print('YES')
        print(n - (k - 1) , str('1 ') * (k - 1))
    else:
        print('NO')
            