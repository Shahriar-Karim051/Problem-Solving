

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
        s = 0
        cnt = 0
        print('novo calculo (1-sim 2-nao)')
        while 1:
            b = input()
            if b != '1' and b !='2':
               print('novo calculo (1-sim 2-nao)')
            else:
                break
        if b == '2':
           break
        
    
    