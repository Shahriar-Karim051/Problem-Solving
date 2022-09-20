
a , b = input().split()
a = int(a)
b = int(b)
l = []
x = [int(x) for x in input().split()]

if len(set(x)) < b:
    print('NO')
else:
    print('YES')
    for i in range(a):
        if x[i] not in l:
            l.append(x[i])
            print(i + 1, end = ' ')
        if len(l) >= b:
            break
        