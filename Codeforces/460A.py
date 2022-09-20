
a , b = input().split()

a = int(a)
b = int(b)

cnt = d = 0
while a > 0:
    a = a - 1
    cnt = cnt + 1
    d = d + 1
    if cnt == b:
        a = a + 1
        cnt = 0
        
print(d)