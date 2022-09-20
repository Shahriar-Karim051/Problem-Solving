
x = [float(x) for x in input().split()]

a = x [0]
b = x[1]
c = x[2]


x.sort()

if x[0] + x[1] > x[2]:
    peri = x[0] + x[1] + x[2]
    print("Perimetro =" , '%.1f'%peri)
else:
    area = 0.5 * (a + b) * c
    print("Area =" , '%.1f'%area)