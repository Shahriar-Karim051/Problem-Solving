
import math
a , b , c = input().split()

a = float(a)
b = float(b)
c = float(c)

d = (b * b) - (4 * a * c)

if a == 0:
    print("Impossivel calcular")
elif d < 0:
    print("Impossivel calcular")
else:
    r1 = (- b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("R1 =" , '%.5f'%r1)
    print("R2 =" , '%.5f'%r2)
    