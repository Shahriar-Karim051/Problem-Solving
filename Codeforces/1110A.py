
b , k = map(int , input().split())
a = [int(a) for a in input().split()]
odd = 0
if b % 2 == 0:
    if a[-1] % 2 == 0:
        print('even')
    else:
        print('odd')
else:
    for i in range(k):
        if a[i] % 2 != 0:
            odd += 1
    if odd % 2 == 0:
        print('even')
    else:
        print('odd')