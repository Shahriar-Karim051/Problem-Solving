
a = int(input())

b = [100,50,20,10,5,2,1]
print(a)
for i in b:
    c = a // i
    print(c , 'nota(s) de R$ ' + str(i) + ',00')
    a = a % i
    