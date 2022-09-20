

a = input()

c = a.count('2') + a.count('3') + a.count('5') + a.count('6') + a.count('7') + a.count('8') + a.count('9') + a.count('0') + a.count('444')

if a[0] != '1':
    print('NO')
elif c == 0:
    print('YES')
else:
    print('NO')