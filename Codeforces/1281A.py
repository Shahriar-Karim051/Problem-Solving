

for i in range(int(input())):
    a = input()
    b = a[-2:]
    if b == 'po':
        print('FILIPINO')
    elif b == 'su':
        print('JAPANESE')
    else:
        print('KOREAN')