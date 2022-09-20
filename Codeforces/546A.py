
a , b , c = input().split()

a = int(a)
b = int(b)
c = int(c)

z = ((((c + 1) * c) // 2) * a) - b

if z > 0:
    print(z)
else:
    print(0)