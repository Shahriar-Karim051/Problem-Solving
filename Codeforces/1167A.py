
n = int(input())

for i in range(n):
    a = input()
    b = input()
    for i in b:
        c = b[b.find('8') :]
    if len(c) >= 11:
        print('YES')
    else:
        print('NO')