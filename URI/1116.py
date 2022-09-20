
n = int(input())

for i in range(n):
    a , b = input().split()
    a = int(a)
    b = int(b)
    if b == 0:
        print('divisao impossivel')
    else:
        div = a / b
        print('%.1f'%div)