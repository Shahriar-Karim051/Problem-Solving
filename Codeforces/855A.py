l = []
for i in range(int(input())):
    a = input()
    if a not in l:
        print('NO')
        l.append(a)
    else:
        print('YES')