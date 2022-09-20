
x = [float(x) for x in input().split()]

x.sort(reverse = True)

if x[0] >= x[1] + x[2]:
    print("NAO FORMA TRIANGULO")
elif (x[0] * x[0]) == (x[1] * x[1]) + (x[2] * x[2]):
    print("TRIANGULO RETANGULO")
elif (x[0] * x[0]) > (x[1] * x[1]) + (x[2] * x[2]):
    print("TRIANGULO OBTUSANGULO")
elif (x[0] * x[0]) < (x[1] * x[1]) + (x[2] * x[2]):
    print("TRIANGULO ACUTANGULO")
    
    
if x[0] == x[1] == x[2]:
    print("TRIANGULO EQUILATERO")
elif x[0] == x[1] != x[2] or x[0] == x[2] != x[1] or x[1] == x[2] != x[0]:
    print("TRIANGULO ISOSCELES")