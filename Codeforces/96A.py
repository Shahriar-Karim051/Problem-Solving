#x = [int(x) for x in input().split()]

x = input()
a = '1111111'
b = '0000000'

if a in x or b in x:
    print('YES')
else:
    print('NO')