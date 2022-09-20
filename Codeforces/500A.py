
a , b = input().split()
b = int(b)
x = [int(x) for x in input().split()]

c = 0

while c < b - 1:
    c = x[c] + c
    
if c == b - 1:
    print('YES')
else:
    print('NO')
    