

x = float(input())



print('NOTAS:')

d = x // 100
print(int(d) , 'nota(s) de R$ 100.00')
x = x % 100
    
d = x // 50
print(int(d) , 'nota(s) de R$ 50.00')
x = x % 50

d = x // 20
print(int(d) , 'nota(s) de R$ 20.00')
x = x % 20

d = x // 10
print(int(d) , 'nota(s) de R$ 10.00')
x = x % 10

d = x // 5
print(int(d) , 'nota(s) de R$ 5.00')
x = x % 5

d = x // 2
print(int(d) , 'nota(s) de R$ 2.00')
x = x % 2
 
print("MOEDAS:")

d = x // 1.00
print(int(d) , 'moeda(s) de R$ 1.00')
x = x % 1.00

d = x // 0.50
print(int(d) , 'moeda(s) de R$ 0.50')
x = x % 0.50

d = x // 0.25
print(int(d) , 'moeda(s) de R$ 0.25')
x = x % 0.25

d = x // 0.10
print(int(d) , 'moeda(s) de R$ 0.10')
x = x % 0.10

d = x // 0.05
print(int(d) , 'moeda(s) de R$ 0.05')
x = x % 0.05

d = x // 0.01
print(int(d) , 'moeda(s) de R$ 0.01')
