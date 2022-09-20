
a = int(input())
 
b = int(input())

c = int(input())

s = t = p = 0

if a == 1 or b == 1 or c == 1:
    p = a + b + c
    s = (a + b) * c
    t = a * (b + c)
    if s > t and s > p:
        print(s)
    elif p > s and p > t:
        print(p)
    else:
        print(t)
else:
    print(a * b * c)