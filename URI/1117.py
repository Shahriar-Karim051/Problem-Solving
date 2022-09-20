
s = cnt = 0
while 1:
    a = float(input())
    if a >= 0 and a <=10:
        s = s + a
        cnt = cnt + 1
    else:
        print('nota invalida')
    if cnt == 2:
        avg = s / 2
        print('media =' , '%.2f'%avg)
        break