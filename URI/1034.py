

alc = gas = die = 0

while 1:
    a = int(input())
    if  a == 1:
        alc = alc + 1
    elif a == 2:
        gas = gas + 1
    elif a == 3:
        die = die + 1
    elif a == 4:
        break
    
print('MUITO OBRIGADO')
print('Alcool:' , alc)
print('Gasolina:' , gas)
print('Diesel:' , die)