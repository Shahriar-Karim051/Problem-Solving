
a , b = input().split()

a = int(a)
b = int(b)
cnt = cn = 0
while a > 0:
    a = a - 1
    cnt = cnt + 1
    cn = cn + 1
    if cn == b:
        a = a + 1
        cn = 0
    
        
print(cnt)