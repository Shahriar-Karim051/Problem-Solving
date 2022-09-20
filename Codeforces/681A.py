d = 0
for i in range(int(input())):
    a , b , c = input().split()
    b = int(b)
    c = int(c)
    if b >= 2400 and b < c:
        d = 1
        
print('YES' if d == 1 else 'NO')