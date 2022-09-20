
a = input()
x = list(a)

b = input()
y = list(b)

c = ['a' , 'e' , 'i' , 'o' , 'u']


if len(x) != len(y):
    print('NO')
    exit()

for i in range(len(x)):
    if x[i] not in c and y[i] in c:
        print('NO')
        exit()
    if x[i] in c and y[i] not in c:
        print('NO')
        exit()
        
print('YES')