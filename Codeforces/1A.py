
n1, m1, a1 = input().split()

n = int(n1)
m = int(m1)
a = int(a1)

if n % a == 0:
    x = n // a
else:
    x = (n // a) + 1
    
if m % a == 0:
    y = m // a
else:
    y = (m // a) + 1

print(x * y)
    
