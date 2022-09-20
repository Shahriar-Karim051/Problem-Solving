
c = ['a' , 'e' , 'i' , 'o' , 'u' , 'y']
n = input()

b = n.index('?')

while n[b - 1] == ' ':
    b -= 1

print('YES' if n[b - 1].lower() in c else 'NO')
