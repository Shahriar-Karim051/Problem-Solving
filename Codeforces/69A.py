
x = int(input())
suma = sumb = sumc = 0
for i in range(x):
    a , b , c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    suma = suma + a
    sumb = sumb + b
    sumc = sumc + c
    
    
if suma == 0 and sumb == 0 and sumc == 0:
    print("YES")
else:
    print("NO")