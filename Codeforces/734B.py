

a , b , c , d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

x = min(a , c , d) * 256

a = a - min(a , c , d)

if a > 0:
    y = min(a , b) * 32
    print(x + y)
else:
    print(x)