
a , b , c = input().split()

b = int(b)
c = float(c)

x , y , z = input().split()

y = int(y)
z = float(z)

total = (b * c) + (y * z)

print("VALOR A PAGAR: R$ " + '%.2f'%total )