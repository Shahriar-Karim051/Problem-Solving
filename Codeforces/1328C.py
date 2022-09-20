
n = int(input())

for i in range(n):
    s = input()
    a = input()
    x = ''
    y = ''
    for i in a:
        if i == '0':
            x += '0'
            y += '0'
        elif i == '1':
            x += '1'
            y += '0'
        else:
            x += '1'
            y += '1'
    print(x)
    print(y)
        
        