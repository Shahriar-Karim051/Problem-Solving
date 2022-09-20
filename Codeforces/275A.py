

x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
z = [int(z) for z in input().split()]

a1 = x[0] + x[1] + y[0]
if a1 % 2 == 0:
    a1 = 1
else:
    a1 = 0
a2 = sum(x) + y[1]
if a2 % 2 == 0:
    a2 = 1
else:
    a2 = 0

a3 = x[1] + x[2] + y[2]
if a3 % 2 == 0:
    a3 = 1
else:
    a3 = 0


b1 = x[0] + y[0] + z[0] + y[1]
if b1 % 2 == 0:
    b1 = 1
else:
    b1 = 0

b2 = sum(y) + x[1] + z[1]
if b2 % 2 == 0:
    b2 = 1
else:
    b2 = 0

b3 = x[2] + y[1] + y[2] + z[2]
if b3 % 2 == 0:
    b3 = 1
else:
    b3 = 0


c1 = y[0] + z[0] + z[1]
if c1 % 2 == 0:
    c1 = 1
else:
    c1 = 0

c2 = sum(z) + y[1]
if c2 % 2 == 0:
    c2 = 1
else:
    c2 = 0

c3 = y[2] + z[1] + z[2]
if c3 % 2 == 0:
    c3 = 1
else:
    c3 = 0


print(str(a1) + str(a2) + str(a3))
print(str(b1) + str(b2) + str(b3))
print(str(c1) + str(c2) + str(c3))
