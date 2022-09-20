
a , b , c = input().split()

a = float(a)

b = float(b)

c = float(c)

tri = 0.5 * a * c
print("TRIANGULO: " + '%.3f'%tri)

cir = 3.14159 * c * c
print("CIRCULO: " + '%.3f'%cir)

tra = 0.5 * (a + b) * c
print("TRAPEZIO: " + '%.3f'%tra)

qua = b * b
print("QUADRADO: " + '%.3f'%qua)

ret = a * b
print("RETANGULO: " + '%.3f'%ret)
