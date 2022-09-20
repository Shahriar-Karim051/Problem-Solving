
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if f > e:
    mn = min(b , c , d)
    d -= mn
    print(mn * f + min(a , d) * e)
else:
    mn = min(a , d)
    d -= mn
    print(mn * e + min(b , c , d) * f)
    