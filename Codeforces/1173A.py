

a , b , c = map(int , input().split())

if a > b:
    if a > b + c:
        print('+')
    else:
        print('?')
elif a < b:
    if a + c < b:
        print('-')
    else:
        print('?')
elif a == b:
    if c == 0:
        print(0)
    else:
        print('?')