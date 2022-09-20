
n = int(input())

for i in range(n):
    a = int(input())
    s = 0
    for j in range(1, a):
        if a % j == 0:
            s = s + j
    if s == a:
        print(a , 'eh perfeito')
    else:
        print(a , 'nao eh perfeito')
    