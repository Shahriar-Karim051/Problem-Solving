

while 1:
    a , b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        break
    if a < b:
        print('Crescente')
    else:
        print('Decrescente')