
n = int(input())

for i in range(n):
    a = input()
    b = input()
    c = input()
    s = 0
    for j in range(len(a)):
        if a[j] != c[j] and b[j] != c[j]:
            s = 1
            break
    if s == 1:
        print('NO')
    else:
        print('YES')
        