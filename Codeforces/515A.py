
a , b , s = input().split()

a = int(a)
a = abs(a)
b = int(b)
b = abs(b)
s = int(s)


if a + b <= s and (a + b - s) % 2 == 0:
    print('YES')
else:
    print('NO')