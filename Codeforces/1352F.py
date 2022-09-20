

for i in range(int(input())):
    n0 , n1 , n2 = map(int , input().split())
    r = ''
    if n1 == 0:
        if n0 == 0:
            print('1' * (n2 + 1))
        elif n1 == 0:
            print('0' * (n0 + 1))
        else:
            print('0' * (n0 + 1) + '1' * (n2 + 1))
    elif n0 == 0 and n2 == 0:
        for j in range(n1 + 1):
            if j % 2 == 0:
                r += '1'
            else:
                r += '0'
        print(r)
    else:
        for j in range(n1 + 1):
            if j % 2 == 0:
                r += '1'
            else:
                r += '0'
        a = list(r)
        a.insert(1 , '0' * n0)
        a.insert(0 , '1' * n2)
        print(''.join(a))
            