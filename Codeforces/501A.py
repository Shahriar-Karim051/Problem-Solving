

a , b , c , d = map(int , input().split())

e = max(3 * (a // 10) , a - ((a // 250) * c))

f = max(3 * (b // 10) , b - ((b // 250) * d))

if e > f:
    print('Misha')
elif e < f:
    print('Vasya')
else:
    print('Tie')