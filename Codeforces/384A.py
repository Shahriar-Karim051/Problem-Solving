

a = int(input())

if a == 1:
    print(1)
    print('C')
else:
    if a % 2 != 0:
        print((pow(a , 2) + 1) // 2)
        for i in range(a):
            if i % 2 == 0:
                print('C.' * (a // 2) + 'C')
            else:
                print('.C' * (a // 2) + '.')
    else:
        print(pow(a , 2) // 2)
        for i in range(a):
            if i % 2 == 0:
                print('C.' * (a // 2))
            else:
                print('.C' * (a // 2) )