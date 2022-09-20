

for i in range(int(input())):
    l = []
    cnt = 0
    a = input()
    b = len(a)
    for j in range(len(a)):
        b = b - 1
        if a[j] != '0':
            r = a[j] + '0' * b
            l.append(r)
            cnt = cnt + 1
    print(cnt)
    for k in l:
        print(str(k) , end = ' ')