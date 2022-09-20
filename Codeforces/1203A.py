
for i in range(int(input())):
    a = int(input())
    x = [int(x) for x in input().split()]
    x.extend(x)
    c = n = d = 1
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            c += 1
            n = 1
            if c >= a:
                print('YES')
                d = 2
                break
        else:
            n += 1
            c = 1
            if n >= a:
                print('YES')
                d = 2
                break
    if d == 1:
        print('NO')